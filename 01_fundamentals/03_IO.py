# beginner_io_operations_in_python.py

"""
===================================
📘 WHAT IS INPUT AND OUTPUT (I/O)?
===================================

📥 Input: Taking data **from the user**
📤 Output: Displaying data **to the user**

Python has:
    👉 input()  — for taking input (always returns a string)
    👉 print()  — for displaying output
"""

# ---------------------------------
# ✅ Example: Simple Input and Output
# ---------------------------------
name = input("Enter your name: ")   # Takes input from the user
print("Hello,", name)              # Prints the greeting

# ---------------------------------
# ⚠️ input() always returns a string!
# ---------------------------------
# If you want to do math, convert it:
num1 = input("Enter a number: ")      # e.g., user enters: 10
num2 = input("Enter another number:") # e.g., user enters: 5

# ❌ This will join them like text:
print("Wrong Sum:", num1 + num2)  # Output: 105

# ✅ Convert to integers before adding:
sum = int(num1) + int(num2)
print("Correct Sum:", sum)        # Output: 15

# ---------------------------------------
# 🔥 TRICKY QUESTION 1: Input + int Error
# ---------------------------------------

# What happens here if the user types: "hello"?
try:
    age = int(input("Enter your age: "))
    print("Q1 Output:", age)
except ValueError as e:
    print("Q1 Error:", e)

# ✅ Always validate user input when converting


# ---------------------------------------
# 🔥 TRICKY QUESTION 2: Mixing input and print
# ---------------------------------------

# What’s the output?
x = input("Q2: Type something: ")
print("You typed:", x)

# Try typing a number vs a word — what’s the type?


# ---------------------------------------
# 🔥 TRICKY QUESTION 3: Multiline Output
# ---------------------------------------

print("Q3 Output:\nLine 1\nLine 2\nLine 3")
# \n means "new line"


# ---------------------------------------
# 🔥 TRICKY QUESTION 4: Print with custom separator
# ---------------------------------------

print("Q4 Output:")
print("Python", "is", "fun", sep="-")  # Output: Python-is-fun


# ---------------------------------------
# 🔥 TRICKY QUESTION 5: Print without newline
# ---------------------------------------

print("Q5 Output:", end=" ")
print("Hello", end=" ")
print("World")  # Output: Hello World

# 🧠 By default, print() adds a new line. `end=" "` lets you change that.

# ---------------------------------------
# 🔥 TRICKY QUESTION 6: Input with custom prompt
name, age, gender = input("Q6: Enter your name, age, and gender (separated by commas): ").split(",")
print("Hello,", name)
print("You are", age, "years old.")
print("Your gender is", gender)