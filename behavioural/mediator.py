'''
Mediator

College objects interact with each other through a mediator object, rather than communicating directly. The mediator acts as a central hub, coordinating the communication and enforcing the rules and protocols of the interaction.

Mediator vs Observer
- The mediator is an object attached as a plug-in to facilitate communication between two or more objects that don't have any knowledge of each other. The users are still the ones that initiate communication.
- Observer is a subscriber / messaging system, where the observer initiates communication with the subscribers. There are no properties on the user objects to indicate which observers they are subscribed to. They also cannot initiate communication.
'''


class Mediator:
    def register_colleague(self, colleague):
        pass

    def send_message(self, message, sender):
        pass


class ChatRoomMediator(Mediator):
    def __init__(self):
        self.colleagues = []

    def register_colleague(self, colleague):
        self.colleagues.append(colleague)

    def send_message(self, message, sender):
        for colleague in self.colleagues:
            if colleague != sender:
                colleague.receive_message(message)


class Colleague:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def send(self, message):
        self.mediator.send_message(message, self)

    def receive_message(self, message):
        print(f"{self.name} received message: {message}")


mediator = ChatRoomMediator()

colleague1 = Colleague("John", mediator)
colleague2 = Colleague("Alice", mediator)

mediator.register_colleague(colleague1)
mediator.register_colleague(colleague2)

colleague1.send("Hello, Alice!")
colleague2.send("Hi, John!")
