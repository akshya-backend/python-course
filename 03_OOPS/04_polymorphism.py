"""
Polymorphism in Python
----------------------

📌 Meaning:
------------
Polymorphism comes from the Greek words 'poly' (many) and 'morph' (form/shape).
It means 'many forms'.

In OOP, polymorphism allows the same function/method name to behave differently
depending on the object or data type calling it.

Think of a single "shape" word — circle, square, triangle — they are all shapes,
but each "draws" differently.

💡 Key points:
--------------
1. Method polymorphism → same method name, different behavior for different objects.
2. Function polymorphism → built-in functions working on different data types.
3. Operator overloading → same operator symbol behaving differently for different objects.
4. Inheritance-based polymorphism → subclass overrides parent's method.
"""

# ----------------------------------------------------
# 1. Function Polymorphism
# ----------------------------------------------------
print("=== FUNCTION POLYMORPHISM ===")
print(len("Hello"))      # len() works with strings → counts characters
print(len([1, 2, 3]))    # len() works with lists → counts elements
print(len({"a": 1, "b": 2}))  # len() works with dictionaries → counts keys

# ----------------------------------------------------
# 2. Method Polymorphism via Inheritance
# ----------------------------------------------------
print("\n=== METHOD POLYMORPHISM ===")

class Bird:
    def speak(self):
        return "Chirp"

class Dog:
    def speak(self):
        return "Woof"

animals = [Bird(), Dog()]
for animal in animals:
    # The same method name 'speak' works differently for each object
    print(animal.speak())

# ----------------------------------------------------
# 3. Inheritance + Method Overriding (Runtime Polymorphism)
# ----------------------------------------------------
print("\n=== RUNTIME POLYMORPHISM (Method Overriding) ===")

class Vehicle:
    def start(self):
        print("Starting vehicle...")

class Car(Vehicle):
    def start(self):
        print("Starting car with a key...")

class Bike(Vehicle):
    def start(self):
        print("Starting bike with a button...")

vehicles = [Car(), Bike()]
for v in vehicles:
    v.start()  # Different output depending on object type

# ----------------------------------------------------
# 4. Operator Overloading (Compile-time Polymorphism in Python's way)
# ----------------------------------------------------
print("\n=== OPERATOR OVERLOADING ===")

class Book:
    def __init__(self, pages):
        self.pages = pages

    # Overloading '+' operator
    def __add__(self, other):
        return self.pages + other.pages

b1 = Book(100)
b2 = Book(200)
print("Total pages:", b1 + b2)  # Uses __add__ method

# ----------------------------------------------------
# 5. Same Interface, Different Implementation
# ----------------------------------------------------
print("\n=== SAME INTERFACE, DIFFERENT IMPLEMENTATION ===")

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        import math
        return math.pi * self.r ** 2

shapes = [Rectangle(10, 20), Circle(5)]
for s in shapes:
    print(f"Area: {s.area()}")  # Same method name, different calculation

"""
💡 Summary:
------------
- Polymorphism lets you write flexible, reusable code.
- It reduces the need to know the exact object type before using it.
- Achieved via:
  ✅ Method overriding (Runtime polymorphism)
  ✅ Built-in function polymorphism
  ✅ Operator overloading
  ✅ Interfaces / abstract methods (via abc module)
"""
