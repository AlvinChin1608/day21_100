# day21_100
I am currently engaged in a 100-day Python Bootcamp, which I am documenting and sharing my progress on GitHub. The boot camp is designed to progressively intensify, allowing me to deepen my understanding and proficiency in Python programming.

Additionally, I have chosen to include the beginner stage and later on intermediate and advanced in my documentation to provide a valuable reference for my future growth and development.

-------------

## Build the Snake Game - Part 2
✅ Create a snake body

✅ Move the snake

✅ Control the snake

✅ Detect Collision with food

✅ Create a scoreboard

✅ Detect collision with wall

✅ Detect collision with tail

---------------
## Introduction to Class Inheritance in Python

Class inheritance is a fundamental concept in object-oriented programming (OOP) that allows you to create new classes based on existing ones. It provides a way to reuse code and create hierarchical relationships between classes.

Here's a breakdown of the key aspects of class inheritance:

**1. Base Class and Derived Class:**

- The existing class from which you inherit properties and behaviors is called the base class (also known as parent class or superclass).
- The new class you create that inherits from the base class is called the derived class (also known as child class or subclass).
```python
class BaseClass:
    # Base class code

class SubClass(BaseClass):
    # Subclass code
```
**2. Inheritance Relationship:**

- The derived class inherits all the public methods (functions) and attributes (variables) from the base class.
- The derived class can also add its own methods and attributes, specializing the inherited functionality.
```python
class Animal:  # Base class
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):  # Derived class inheriting from Animal
    def __init__(self, name, breed):
        super().__init__(name)  # Call the base class constructor
        self.breed = breed

    def make_sound(self):  # Overriding the inherited method
        print("Woof!")

my_dog = Dog("Fido", "Labrador")
my_dog.make_sound()  # Output: Woof!
```
In this example, Dog inherits from Animal and gains access to its name attribute and make_sound method. However, Dog overrides the make_sound method to provide a specific sound for a dog.

## Terminology:

**- Inheritance:** The act of creating a new class based on an existing class.
**- Subclass:** A class that inherits from another class (derived class).
**- Superclass:** A class that is inherited from (base class).
**- Is-A Relationship:** A derived class represents a more specific type of the base class. In simpler terms, objects of the derived class can be considered as a special kind of object of the base class (e.g., a RacingCar is a type of Car).

## Benefits of Inheritance:

**- Code Reuse:** You can avoid writing the same code repeatedly by inheriting from a base class.
**- Extensibility:** Derived classes can add new functionality without modifying the base class.
**- Maintainability:** Changes made to the base class are automatically reflected in derived classes unless overridden.
**- Polymorphism:** Derived classes can provide different implementations for inherited methods, allowing for flexible behavior.
