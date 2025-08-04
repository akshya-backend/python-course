# beginner_variables_with_examples.py

"""
====================================
📘 PYTHON VARIABLES — FULL GUIDE
====================================

🔹 A variable is a **name** that stores a value.
🔹 Python variables are **dynamically typed** — no need to declare a type.

👉 Examples:
    x = 5               # Integer
    name = "Samantha"   # String
    pi = 3.14           # Float

Variables act as **labels for data** you want to store and reuse.
"""

# -------------------------------
# ✅ BASIC ASSIGNMENT
# -------------------------------

x = 5
name = "Samantha"
print(x)       # Output: 5
print(name)    # Output: Samantha


# -------------------------------
# ✅ RULES FOR NAMING VARIABLES
# -------------------------------
# ✅ Can contain letters, numbers, underscores (_)
# ❌ Cannot start with a number
# ❌ Cannot use Python keywords
# ✅ Case-sensitive (name ≠ Name)

age = 21
_colour = "lilac"
total_score = 90
# ❌ 1name = "Error"
# ❌ class = 10
# ❌ user-name = "Doe"


# -------------------------------
# ✅ MULTIPLE ASSIGNMENTS
# -------------------------------

# Same value to multiple variables
a = b = c = 100
print(a, b, c)   # Output: 100 100 100

# Different values to multiple variables
x, y, z = 1, 2.5, "Python"
print(x, y, z)   # Output: 1 2.5 Python


# -------------------------------
# ✅ TYPE CASTING
# -------------------------------

# Converting data types using int(), float(), str()
s = "10"
n = int(s)           # string → int
cnt = 5
f = float(cnt)       # int → float
age = 25
s2 = str(age)        # int → string

print(n)    # 10
print(f)    # 5.0
print(s2)   # '25'


# -------------------------------
# ✅ TYPE CHECKING WITH type()
# -------------------------------

n = 42
f = 3.14
s = "Hello"
li = [1, 2, 3]
d = {'key': 'value'}
b = True

print(type(n))  # <class 'int'>
print(type(f))  # <class 'float'>
print(type(s))  # <class 'str'>
print(type(li)) # <class 'list'>
print(type(d))  # <class 'dict'>
print(type(b))  # <class 'bool'>


# -------------------------------
# ✅ OBJECT REFERENCES
# -------------------------------

x = 5
y = x     # y refers to the same object
x = "Geeks"  # x now refers to a new string
y = "Computer"

# Memory-wise:
# x → "Geeks"
# y → "Computer"
# Old int 5 has no reference now (garbage collected)


# -------------------------------
# ✅ DELETE VARIABLE WITH del
# -------------------------------

x = 10
print(x)
del x
# print(x)  # ❌ NameError: x is not defined


# -------------------------------
# 🔥 TRICKY QUESTION #1: Case Sensitivity
# -------------------------------

Name = "Python"
name = "Java"
print("Q1 Output:", Name, name)  # Python Java


# -------------------------------
# 🔥 TRICKY QUESTION #2: Reassign Type
# -------------------------------

value = 100
print("Q2:", value)
value = "Now a string"
print("Q2 Changed:", value)


# -------------------------------
# 🔥 TRICKY QUESTION #3: Overwriting Built-ins
# -------------------------------

sum = 50
try:
    result = sum([1, 2, 3])  # ❌ TypeError: 'int' object is not callable
except Exception as e:
    print("Q3 Error:", e)


# -------------------------------
# 🔥 TRICKY QUESTION #4: Undefined Variable
# -------------------------------
score=12
try:
    print("Q4:", score)
except NameError as e:
    print("Q4 Error:", e)

score = 90


# -------------------------------
# 🔥 TRICKY QUESTION #5: Swapping Variables
# -------------------------------

a, b = 5, 10
a, b = b, a
print("Q5 Swapped:", a, b)  # Output: 10 5


# -------------------------------
# ✅ PRACTICAL EXAMPLE
# -------------------------------

word = "Python"
length = len(word)
print("Length of the word:", length)  # Output: 6

# Python holds references to objects — not the actual values directly in variables.

x = 10
y = x
x = 20
print(y)       # 10
print(x)       # 20
print(x is y)  # False now


#  2nd example
a = [1, 2, 3]
b = a
b.append(4)

print(a)  # [1, 2, 3, 4] — changed!
print(b)  # [1, 2, 3, 4]
