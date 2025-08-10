"""
📄 Concept: Inheritance in Python

📝 What you'll learn:
- How to inherit from another class
- Using super() to call parent constructor
- Method overriding
"""

# Parent class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        return f"{self.brand} is moving"

# Child class
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Call parent __init__
        self.model = model

    # Overriding method
    def drive(self):
        return f"{self.brand} {self.model} is driving smoothly"

# Creating objects
vehicle1 = Vehicle("Generic Vehicle")
car1 = Car("Tesla", "Model X")

print(vehicle1.drive())  # Generic Vehicle is moving
print(car1.drive())      # Tesla Model X is driving smoothly

"""
💡 Key Notes:
1. Inheritance allows code reusability.
2. super() calls the parent class's methods/constructors.
3. Method overriding lets the child class change parent behavior.
"""
