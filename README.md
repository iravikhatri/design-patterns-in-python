# Object-Oriented Design Patterns in Python

This repository provides a basic implementation of various Object-Oriented Design Patterns in Python. Design patterns are reusable solutions to common software design problems. They provide proven solutions to recurring design challenges, making our code more flexible, maintainable, and scalable.

## Available Design Patterns

The following design patterns are implemented in this repository:

### Creational Patterns:

1. **Singleton Pattern:** Ensures that a class has only one instance and provides a global point of access to it.

2. **Factory Pattern:** Provides an interface for creating objects, but allows subclasses to decide which class to instantiate.

3. **Abstract Factory Pattern:** Provides an interface for creating families of related or dependent objects without specifying their concrete classes.

4. **Builder Pattern:** Separates the construction of an object from its representation, allowing the same construction process to create different representations.

5. **Prototype Pattern:** Creates new objects by cloning an existing object, allowing for object creation without specifying their exact class.

### Structural Patterns:

6. **Adapter Pattern:** Allows objects with incompatible interfaces to work together by providing a wrapper with a compatible interface.

7. **Bridge Pattern:** Decouples an abstraction from its implementation, allowing the two to vary independently.

8. **Composite Pattern:** Composes objects into tree-like structures to represent part-whole hierarchies. It allows clients to treat individual objects and compositions uniformly.

9. **Decorator Pattern:** Dynamically adds new behavior to objects by wrapping them with additional functionality.

10. **Facade Pattern:** Provides a simplified interface to a complex subsystem, making it easier to use and understand.

11. **Flyweight Pattern:** Minimizes memory usage by sharing common data between multiple similar objects.

12. **Proxy Pattern:** Provides a surrogate or placeholder for another object to control access to it.


### Behavioral Patterns:

13. **Chain of Responsibility Pattern:** Allows an object in a chain to handle a request and pass it on to the next handler in the chain until the request is handled.

14. **Command Pattern:** Encapsulates a request as an object, allowing parameterization of clients with different requests, queueing or logging requests, and support for undoable operations.

15. **Iterator Pattern:** Provides a way to access elements of an aggregate object sequentially without exposing its underlying representation.

16. **Mediator Pattern:** Defines an object that encapsulates how a set of objects interact, promoting loose coupling between the objects.

17. **Memento Pattern:** Captures and restores an object's internal state without violating encapsulation, allowing it to be restored to a previous state.

18. **Observer Pattern:** Defines a one-to-many dependency between objects, so that when one object changes state, all its dependents are notified and updated automatically.

19. **State Pattern:** Allows an object to alter its behavior when its internal state changes, encapsulating the state-specific behavior into separate classes.

20. **Strategy Pattern:** Defines a family of algorithms, encapsulates each one, and makes them interchangeable. The strategy pattern lets the algorithm vary independently from the clients that use it.

21. **Template Method Pattern:** Defines the skeleton of an algorithm in a method, deferring some steps to subclasses. Subclasses can redefine certain steps of the algorithm without changing its structure.

22. **Visitor Pattern:** Separates an algorithm from an object structure, allowing the addition of new operations without modifying the objects.

These patterns cover a wide range of design challenges and provide reusable solutions to common problems in software development. Each pattern has its own purpose and can be used in different contexts to improve the design and maintainability of your code.

## How to Use

Each design pattern is implemented in a separate directory within this repository. Inside each directory, you will find the necessary Python files to understand and use the design pattern.

To use a design pattern:

1. Navigate to the directory of the design pattern you are interested in.
2. Open the Python files in your preferred Python IDE or text editor.
3. Study the code and understand the structure and implementation of the design pattern.
4. Adapt and use the code in your own projects as needed.

Feel free to explore the implementation of different design patterns and experiment with them in your Python projects.