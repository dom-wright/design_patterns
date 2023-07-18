'''
State

There are scenarios where an object will behave very differently depending on their state at a given time. The State pattern seeks to define these different behaviours in separate objects, which can be plugged-in to the host object when required. The host object then delegates the work to the plugged-in object. This achieves loose coupling.

A good indicator if the state pattern would be useful, is if there are a lot of conditional statements within the host's methods that evaluate an attribute on the host itself i.e. evaluate its state to make decisions on actions.

Example:
State in this case could be something like order status e.g. shipped or cancelled below. The ship and cancel methods may behave very differently depending on this state. Extensive conditional loops within every method of the order object can be avoided, and additional / new behaviours can be added more easily.

Other examples incude UI systems, where the screen may be enabled, disabled or read-only, ecommerce systems where an object may be at full price, discounted, or part of an wider offer structure.
'''


class OrderState:
    def ship(self):
        pass

    def cancel(self):
        pass


class NewOrderState(OrderState):
    def ship(self):
        print("Shipping the order...")
        # Transition to the Shipped state
        return ShippedOrderState()

    def cancel(self):
        print("Cancelling the order...")
        # Transition to the Cancelled state
        return CancelledOrderState()


class ShippedOrderState(OrderState):
    def ship(self):
        print("The order has already been shipped.")

    def cancel(self):
        print("Cannot cancel a shipped order.")


class CancelledOrderState(OrderState):
    def ship(self):
        print("Cannot ship a cancelled order.")

    def cancel(self):
        print("The order has already been cancelled.")


class Order:
    def __init__(self):
        # Initial state is New
        self.state = NewOrderState()

    def ship(self):
        self.state = self.state.ship()

    def cancel(self):
        self.state = self.state.cancel()


# Usage example
order = Order()

# shipping the order, changes the state of the order to ShippedOrderState, which has its own ship and cancel implementations.
order.ship()

order.cancel()  # Cancelling the order...
order.ship()  # Cannot ship a cancelled order.

order.cancel()  # The order has already been cancelled.
order.ship()  # Cannot ship a cancelled order.
