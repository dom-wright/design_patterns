'''
Observer

A sort of notification / subscriber system, it allows an object (subjects) to notify other objects (observers) about changes in their state, so they can react accordingly. importantly this can be done without coupling the observers to the subject.

It is used in event handling in the browser (events propagated to various components), MVC architecture when model (data) changes are detected, distributed systems, message passing (publishing of messages), logging and monitoring.

Observer vs Mediator
- Observer is a subscriber / messaging system, where the observer initiates the communication with its subscribers. There are no properties on the user objects to indicate which observers they are subscribed to.
- The mediator is an object attached as a plug-in to facilitate communication between two or more objects that don't have any knowledge of each other. The users are the ones that initiate communication.
'''


class Message:
    def __init__(self, content):
        self.content = content


class MessageBroker:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)

    def publish(self, message):
        for subscriber in self._subscribers:
            subscriber.receive(message)


class Subscriber:
    def __init__(self, name):
        self.name = name

    def receive(self, message):
        print(f"{self.name} received message: {message.content}")


broker = MessageBroker()

subscriber1 = Subscriber("Subscriber 1")
subscriber2 = Subscriber("Subscriber 2")
subscriber3 = Subscriber("Subscriber 3")

broker.subscribe(subscriber1)
broker.subscribe(subscriber2)
broker.subscribe(subscriber3)

message = Message("Hello, everyone!")
broker.publish(message)

broker.unsubscribe(subscriber2)

message = Message("Observer 2 unsubscribed.")
broker.publish(message)
