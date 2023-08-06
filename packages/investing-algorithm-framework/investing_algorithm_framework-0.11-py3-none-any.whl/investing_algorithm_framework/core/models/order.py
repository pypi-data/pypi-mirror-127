import logging
from datetime import datetime
from random import randint

from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from sqlalchemy.orm.base import NO_VALUE
from sqlalchemy import event

from investing_algorithm_framework.core.exceptions import OperationalException
from investing_algorithm_framework.core.models import db, OrderType, \
    OrderStatus
from investing_algorithm_framework.core.models.model_extension \
    import ModelExtension
from .order_side import OrderSide

logger = logging.getLogger(__name__)


def random_id():
    """
    Function to create a random ID. This function checks first if
    the generated ID is not already taken.
    Returns: random integer that can be used as an ID
    """
    minimal = 100
    maximal = 1000000000000000000
    rand = randint(minimal, maximal)

    while Order.query.filter_by(id=rand).first() is not None:
        rand = randint(minimal, maximal)

    return rand


class Order(db.Model, ModelExtension):
    """
        Class AlgorithmOrder: a database model for an AlgorithmOrder instance.

        Attributes:
        An AlgorithmOrder instance consists out of the following attributes:

        - id: unique identification also used externally
        - target_symbol: the target asset symbol of the order
        - trading_symbol: the asset that is traded for the target symbol
        - order side: the side of the order, e.g. BUY or SELL
        - order type: the order type, e.g LIMIT.

        The following attributes are OPTIONAL:

        - price: the price of the target symbol (in trading symbol currency)
        - amount: the amount of the target symbol

        Updated post-execution:

        for all child orders
        - completed_at: DateTime the order was marked as completed

        Relations:

        - position: relation to the AlgorithmPosition instances
        of users subscribed to the algorithm
        """

    __tablename__ = "orders"

    # Integer id for the Order as the primary key
    id = db.Column(
        db.Integer,
        primary_key=True,
        unique=True,
        default=random_id
    )
    order_reference = db.Column(db.Integer)
    target_symbol = db.Column(db.String)
    trading_symbol = db.Column(db.String)

    order_side = db.Column(
        db.String,
        nullable=False,
        default=OrderSide.BUY.value
    )
    order_type = db.Column(
        db.String,
        nullable=False,
        default=OrderType.LIMIT.value
    )

    # The price and amount of the asset
    initial_price = db.Column(db.Float)
    closing_price = db.Column(db.Float)
    amount = db.Column(db.Float)
    amount_trading_symbol = db.Column(db.Float)
    amount_target_symbol = db.Column(db.Float)
    status = db.Column(db.String)

    position_id = db.Column(
        db.Integer, db.ForeignKey('positions.id')
    )
    position = db.relationship("Position", back_populates="orders")

    # Standard date time attributes
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    # Post execution
    executed_at = db.Column(db.DateTime)

    def __init__(
            self,
            order_side,
            order_type,
            target_symbol,
            trading_symbol,
            price=None,
            amount=None,
            amount_target_symbol=None,
            amount_trading_symbol=None,
            **kwargs
    ):
        self.order_side = OrderSide.from_string(order_side).value
        self.order_type = OrderType.from_string(order_type).value
        self.target_symbol = target_symbol
        self.trading_symbol = trading_symbol
        self.status = None
        self.initial_price = price
        self.amount = amount
        self.amount_trading_symbol = amount_trading_symbol
        self.amount_target_symbol = amount_target_symbol

        if OrderType.MARKET.equals(self.order_type):

            if OrderSide.SELL.equals(self.order_side):
                if amount_target_symbol is None:
                    raise OperationalException(
                        "Amount target symbol needs to be set "
                        "for a market sell order"
                    )
            else:
                if amount_trading_symbol is None:
                    raise OperationalException(
                        "Amount trading symbol needs to be set "
                        "for a market buy order"
                    )
        else:
            if self.amount_target_symbol is None:
                raise OperationalException(
                    "Amount target symbol needs to be set "
                    "for limit sell order"
                )

            self.amount_trading_symbol = price * self.amount_target_symbol

        super(Order, self).__init__(**kwargs)

    @validates(
        'id',
        'target_symbol',
        'trading_symbol',
        'order_side',
        'order_type',
    )
    def _write_once(self, key, value):
        existing = getattr(self, key)

        if existing is not None:
            raise ValueError("{} is write-once".format(key))

        return value

    @property
    def current_price(self):
        from investing_algorithm_framework import current_app
        market_service = current_app.algorithm \
            .get_market_service(self.position.portfolio.market)

        current_price = self.initial_price

        try:
            current_price = market_service.get_price(
                self.target_symbol, self.trading_symbol
            )
        except Exception as e:
            logger.error(e)
            return current_price

        return current_price.price

    @hybrid_property
    def delta(self):

        # Delta is 0 if it is a sell order
        if OrderSide.SELL.equals(self.order_side):
            return 0

        if self.closing_price:
            return (self.closing_price * self.amount_target_symbol) - \
                   (self.initial_price * self.amount_target_symbol)

        if not OrderStatus.SUCCESS.equals(self.status):
            return 0

        price = self.current_price

        # With no price data_provider return 0
        if price is None or price == -1:
            return 0

        return (price * self.amount_target_symbol) - \
               (self.initial_price * self.amount_target_symbol)

    @hybrid_property
    def percentage(self):

        if OrderSide.SELL.equals(self.order_side):
            return 0

        if not OrderStatus.SUCCESS.equals(self.status):
            return 0

        portfolio = self.position.portfolio

        return (
           self.current_value /
           (portfolio.allocated + portfolio.unallocated)
        ) * 100

    @hybrid_property
    def percentage_position(self):

        if OrderSide.SELL.equals(self.order_side):
            return 0

        if not OrderStatus.SUCCESS.equals(self.status):
            return 0

        return self.amount_target_symbol / self.position.amount * 100

    @hybrid_property
    def percentage_realized(self):

        if OrderSide.SELL.equals(self.order_side):
            return 0

        if not OrderStatus.CLOSED.equals(self.status):
            return 0

        portfolio = self.position.portfolio

        return (self.amount_target_symbol * self.closing_price) \
                / portfolio.realized * 100

    @hybrid_property
    def current_value(self):

        # Current value is 0 if it is a sell order
        if OrderSide.SELL.equals(self.order_side):
            return 0

        if self.status is None or OrderStatus.CANCELED.equals(self.status):
            return 0

        # Order is closed
        if OrderStatus.CLOSED.equals(self.status):
            return self.closing_price * self.amount_target_symbol

        if OrderStatus.PENDING.equals(self.status):
            return self.price * self.amount_target_symbol

        price = self.current_price
        return price * self.amount_target_symbol

    def set_executed(
        self, snapshot=True, executed_at=None, amount=None, price=None
    ):
        if not OrderStatus.PENDING.equals(self.status) and \
                self.status is not None:
            raise OperationalException("Order is not in pending state")

        if self.position is None:
            raise OperationalException("Order is not linked to a position")

        if OrderType.MARKET.equals(self.order_type):
            self.initial_price = price

            if amount is None or price is None:
                raise OperationalException(
                    "Amount and price needs to be provided for execution "
                    "of a market order"
                )

            if OrderSide.SELL.equals(self.order_side):
                self.amount_trading_symbol = amount
            else:
                self.amount_target_symbol = amount

        if executed_at is not None:
            self.executed_at = executed_at
        else:
            self.executed_at = datetime.utcnow()

        if OrderSide.BUY.equals(self.order_side):
            self.status = OrderStatus.SUCCESS.value
            self.position.amount += self.amount_target_symbol
            self.position.cost += \
                self.amount_target_symbol * self.initial_price
            self.position.portfolio.total_cost += self.amount_trading_symbol
        else:
            self.status = OrderStatus.SUCCESS.value
            self.position.amount -= self.amount_target_symbol
            self.position.portfolio.total_revenue += \
                self.initial_price * self.amount_target_symbol

        db.session.commit()

        if snapshot:
            self.snapshot(self.executed_at)

    def set_closed(self, sell_order):
        self.status = OrderStatus.CLOSED.value
        self.closing_price = sell_order.initial_price
        db.session.commit()

    def set_pending(self):

        if not OrderStatus.TO_BE_SENT.equals(self.status):
            raise OperationalException("Order status is not TO_BE_SENT")

        self.status = OrderStatus.PENDING.value
        db.session.commit()

    def update(self, db, data, commit=True, **kwargs):
        self.updated_at = datetime.utcnow()
        super(Order, self).update(db, data, commit, **kwargs)

    def copy(self, amount=None):

        if amount is None:
            amount = self.amount

        if amount > self.amount_target_symbol:
            raise OperationalException("Amount is larger then original order")

        order = Order(
            amount=amount,
            price=self.initial_price,
            order_side=self.order_side,
            order_type=self.order_type,
            target_symbol=self.target_symbol,
            trading_symbol=self.trading_symbol,
            amount_target_symbol=self.amount_target_symbol -
                                 (self.amount_target_symbol - amount),
        )

        order.amount_trading_symbol = order.initial_price \
                                      * order.amount_target_symbol
        order.order_reference = self.order_reference
        order.status = self.status
        order.executed_at = self.executed_at
        order.updated_at = self.updated_at
        order.created_at = self.created_at
        order.closing_price = self.closing_price

        self.amount_trading_symbol -= order.amount_trading_symbol
        self.amount_target_symbol -= order.amount_target_symbol

        return order

    def split(self, amount):

        if not OrderSide.BUY.equals(self.order_side):
            raise OperationalException("Sell order can't be split")

        if not OrderStatus.SUCCESS.equals(self.status):
            raise OperationalException("Order can't be split")

        if amount <= 0 or amount >= self.amount_target_symbol:
            raise OperationalException("Split amount has a wrong value")

        algorithm_order = self.copy(amount=amount)
        self.position.orders.append(algorithm_order)
        db.session.commit()

        return self, algorithm_order

    def save(self, db, commit=True):

        if self.position is None:
            raise OperationalException(
                "Can't save order that is not linked to an position"
            )

        super(Order, self).save(db, commit)

    def cancel(self, commit=True):
        from investing_algorithm_framework import current_app

        if OrderStatus.PENDING.equals(self.status) or \
                OrderStatus.TO_BE_SENT.equals(self.status) or \
                self.status is None:

            market_service = current_app.algorithm \
                .get_market_service(self.position.portfolio.market)

            market_service.cancel_order(self.order_reference)

            self.update(
                db, {"status": OrderStatus.CANCELED.value}, commit=commit
            )

            if OrderSide.BUY.equals(self.order_side):
                self.position.portfolio.unallocated += \
                    self.amount_trading_symbol

            if commit:
                db.session.commit()

            self.snapshot()

    def snapshot(self, creation_datetime=None):
        from investing_algorithm_framework.core.models.snapshots \
            import PortfolioSnapshot
        PortfolioSnapshot \
            .from_portfolio(
                self.position.portfolio,
                creation_datetime=creation_datetime
            ) \
            .save(db)

    def __repr__(self):
        return self.repr(
            id=self.id,
            status=self.status,
            order_side=self.order_side,
            target_symbol=self.target_symbol,
            trading_symbol=self.trading_symbol,
            amount_target_symbol=self.amount_target_symbol,
            amount_trading_symbol=self.amount_trading_symbol,
            price=self.price,
            created_at=self.created_at,
        )


@event.listens_for(Order.status, "set")
def sync_portfolio_and_position(target, value, old_value, initiator):
    if old_value is NO_VALUE:
        return

    if OrderSide.SELL.equals(target.order_side):

        if (old_value is None or OrderStatus.PENDING.equals(old_value)) and \
                OrderStatus.SUCCESS.equals(value):

            sell_amount = target.amount_target_symbol

            # Close open buy orders
            buy_orders = target.position.orders \
                .filter_by(order_side=OrderSide.BUY.value) \
                .filter_by(status=OrderStatus.SUCCESS.value) \
                .order_by(Order.created_at) \
                .all()

            closed_orders = []
            index = 0

            while sell_amount != 0:
                buy_order = buy_orders[index]

                if buy_order.amount_target_symbol <= sell_amount:
                    sell_amount -= buy_order.amount_target_symbol
                    buy_order.set_closed(target)
                    closed_orders.append(buy_order)
                else:
                    remainder = buy_order.amount_target_symbol - sell_amount
                    og, split = buy_order.split(remainder)
                    og.set_closed(target)
                    closed_orders.append(og)
                    sell_amount = 0

                index += 1

            portfolio = target.position.portfolio
            position = target.position

            unallocated = 0
            realized = 0
            cost = 0

            for closed_order in closed_orders:
                unallocated += closed_order.current_value
                realized += closed_order.delta
                cost += \
                    closed_order.amount_target_symbol \
                    * closed_order.initial_price

            position.cost -= cost
            portfolio.unallocated += unallocated
            portfolio.realized += realized
            db.session.commit()
