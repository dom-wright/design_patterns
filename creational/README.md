# Creational

Creational design patterns deal with object creation mechanisms. They provide solutions for creating objects in a flexible, decoupled, and reusable manner.

## Sub-types

| Pattern              | Description                                                                                                                                                                            |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Factory**          | Factory methods are used when the exact concrete implementation required for a task is not known until runtime. Choice of the appropriate object is delegated to a separate component. |
| **Abstract Factory** | Abstract class to build factories. The pattern also provides abstract classes for the types of object being created.                                                                   |
| **Builder**          | Separates the construction of a complex object from the object itself. Creation of the object will be achieved entirely through a separate builder class.                              |
| **Prototype**        | Allows for the cloning of an object, normally through a method on the object itself.                                                                                                   |
| **Singleton**        | Logic which restricts the instantiation of a class to one object, which should be globally accessible in the program.                                                                  |