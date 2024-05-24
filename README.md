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

**Terminology:**

- Inheritance: The act of creating a new class based on an existing class.
- Subclass: A class that inherits from another class (derived class).
- Superclass: A class that is inherited from (base class).
- Is-A Relationship: A derived class represents a more specific type of the base class. In simpler terms, objects of the derived class can be considered as a special kind of object of the base class (e.g., a RacingCar is a type of Car).

**Benefits of Inheritance:**

- Code Reuse: You can avoid writing the same code repeatedly by inheriting from a base class.
- Extensibility: Derived classes can add new functionality without modifying the base class.
- Maintainability: Changes made to the base class are automatically reflected in derived classes unless overridden.
- Polymorphism: Derived classes can provide different implementations for inherited methods, allowing for flexible behavior.

-----------------------------

## Introduction to Python Slicing

Slicing in Python is a powerful way to extract a specific section of a data structure like a list, string, or tuple. It allows you to efficiently access and manipulate subsequences of elements.

Here's a breakdown of the basics:

**1. Slicing Syntax:**
```python
data_structure[start:end:step]
```
- data_structure: This is the list, string, or tuple you want to slice from.
  
- start (optional): This specifies the index of the element where the slice begins (inclusive). Defaults to 0 (beginning of the data structure).
  
- end (optional): This specifies the index of the element where the slice ends (exclusive). Up to, but not including, the element at this index. Defaults to the end of the data structure.
  
- step (optional): This specifies the step size for including elements in the slice. Defaults to 1 (includes every element).

**2. Examples:**

**String Slicing:**
```python
my_string = "Hello, world!"

# Get characters from index 0 (inclusive) to 5 (exclusive):
substring = my_string[0:5]  # Output: "Hello"

# Get everything from index 7 (inclusive) to the end:
substring = my_string[7:]  # Output: "world!"

# Get every other character starting from the beginning:
substring = my_string[::2]  # Output: "Hlo ol!"
```
**List Slicing:**
```python
my_list = [1, 2, 3, 4, 5]

# Get elements from index 1 (inclusive) to 3 (exclusive):
sublist = my_list[1:3]  # Output: [2, 3]

# Get a copy of the entire list (common use case for copying):
copy_list = my_list[:]  # Output: [1, 2, 3, 4, 5]

# Get elements in reverse order (step of -1):
reversed_list = my_list[::-1]  # Output: [5, 4, 3, 2, 1]
```
The best way to describe this 👇

Let's say we only want to print 2-4, we would put it [1:4]
```python
[1,2,3,4,5]
| | | | | |
0 1 2 3 4 5
```
and let's say we only want 1, 3, 5, we would put it [::2] so it skips every step of 2

- Index 0 (step 1): 1
- Index 2 (step 2, skipping 1): 3
- Index 4 (step 3, skipping 2 and 3): 5
