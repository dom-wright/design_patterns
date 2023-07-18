# Structural

Deal with the composition and relationships between objects, and the larger structures they form. They focus on how objects and classes can be combined to form larger structures while keeping the system modular, extensible, and easy to understand.

## Sub-types

| Pattern       | Description                                                                                                                                                          |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Adapter**   | The adapter object allows objects with incompatible interfaces to work together. It is purpose built for the object in question.                                     |
| **Bridge**    | Decouples the abstraction (high-level entity) from its implementation (low-level details or implementation logic).                                                   |
| **Composite** | Arranges objects of the same types into a tree like structure, allowing for the whole structure to be interacted with as one single object.                          |
| **Decorator** | Allows behaviours and attributes to be added / plugged on to an object dynamically.                                                                                  |
| **Facade**    | A high-level interface to a complex subsystem of classes, making it easier to understand and interact with.                                                          |
| **Flyweight** | A form of caching. The flyweight will check if it has already created the desired object and return it if it has, or create it new, add to collection and return it. |
| **Proxy**     | A sort of wrapper class which controls access to the wrapped object.                                                                                                 |