# Behavioural

Behavioural patterns focus on the interaction and delegation of responsibilities between objects, providing solutions for effective communication and collaboration. Some common examples of behavioural patterns are:

| Pattern      | Description                                                                                                                                                                                        |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Chain**    | Passes a request along a chain of potential handlers until the request is handled or reaches the end of the chain                                                                                  |
| **Command**  | Encapsulates a request / action as an object, and uses an invoker class to execute them. The invoker keeps an ordered record of completed actions, enabling undo / redo capability.                |
| **Iterator** | Separates the iteration logic away from the object / structure to be iterated. Allows for multiple simultaneous iterations, and also different iteration strategies to be coded.                   |
| **Mediator** | Objects communicate with each other through a mediator class. The mediator acts as a central hub, coordinating communication and enforcing the rules and protocols of the interaction.             |
| **Memento**  | A class used to store a snapshot of the internal state of an object (called by the object). The snapshot can be restored later, effectively providing the ability to rollback to a previous state. |
| **Observer** | A notification system. Objects register / unregister with the message broker, which will message all when some event it is watching occurs.                                                        |
| **State**    | Allows an object to change its behaviour (methods) when its state (attributes) changes.                                                                                                            |
| **Strategy** | Strategies can be encapsulated in different objects, which can be plugged in / out and used when appropriate.                                                                                      |
| **Template** | A skeleton or outline of an algorithm saved in a base class, which can be extended and personalised for the task at hand. Think Django CBVs.                                                       |
| **Visitor**  | Separates the logic for performing operations on data structures from the structures themselves. Similar, but slightly different implementation to the Strategy pattern.                           |