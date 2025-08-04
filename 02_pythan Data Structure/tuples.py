# ========================================================
# 🐍 PYTHON TUPLES: FULL PRACTICE WORKBOOK (.py FORMAT)
# ========================================================
# Tuples are ordered, immutable collections in Python.
# This workbook includes:
# - Concepts explained simply
# - Code examples
# - TODOs for practice
# ========================================================

# 🔰 1. Introduction to Tuples
# ----------------------------
# Tuples are like lists, but **immutable** (cannot be changed).
# Syntax: tuple_name = (item1, item2, item3)

colors = ("red", "green", "blue")
print(colors)

# ✅ TODO: Create a tuple named 'months' with 4 month names.

# 🧭 Accessing Elements
print(colors[0])       # 'red'
print(colors[-1])      # 'blue'

# ✅ TODO: Access and print the 2nd and last month in your tuple.

# 🌀 Tuple Length
print(len(colors))     # 3

# ✅ TODO: Print the number of months in your 'months' tuple.

# 🔄 Looping through a Tuple
for color in colors:
    print("Color:", color)

# ✅ TODO: Loop through your 'months' tuple and print each one with a custom message.

# 🧊 Tuple Immutability
# colors[0] = "yellow"  ❌ This will raise: TypeError: 'tuple' object does not support item assignment

# ✅ TODO: Try changing a value in your tuple and observe the error.

# 🔄 One-Item Tuples
# Must include a comma: ("apple",)
single = ("only_one",)
not_a_tuple = ("only_one")  # This is just a string!

print(type(single))        # tuple
print(type(not_a_tuple))   # str

# ✅ TODO: Create a one-item tuple of your favorite number and print its type.

# 🧮 Tuple Methods
numbers = (1, 2, 2, 3, 4, 4, 4, 5)
print(numbers.count(4))      # 3
print(numbers.index(2))      # 1

# ✅ TODO: Count how many times a value appears in a tuple of your choice.

# 🎯 Tuple Packing & Unpacking
person = ("John", 25, "Engineer")
name, age, profession = person
print(name, age, profession)

# ✅ TODO: Create a tuple of your (name, age, city) and unpack it.

# 🧩 Tuples Inside Lists & Vice Versa
list_of_tuples = [("a", 1), ("b", 2)]
tuple_of_lists = ([1, 2], [3, 4])

print(list_of_tuples[0][1])    # 1
print(tuple_of_lists[1][0])    # 3

# ✅ TODO: Create a list of 3 subject-grade tuples like ("Math", 90)

# ➕ Concatenation & Repetition
a = (1, 2)
b = (3, 4)
c = a + b
print(c)

d = a * 3
print(d)  # (1, 2, 1, 2, 1, 2)

# ✅ TODO: Concatenate your 'months' tuple with another 2-month tuple.

# 📚 Using Tuples as Dictionary Keys
grades = {("Math", "John"): 90, ("Math", "Alice"): 95}
print(grades[("Math", "Alice")])

# ✅ TODO: Create a dictionary where keys are (subject, student) tuples and values are marks.

# 🎲 Tuple vs List: When to Use
# ------------------------------
# Use a tuple when:
# - The data should not be modified (e.g. coordinates, days of week)
# - It needs to be hashable (used as a dictionary key or in a set)

# ✅ TODO: Write a comment example when you would prefer a tuple over a list.

# 🔄 Convert Between Tuple and List
my_list = [10, 20, 30]
my_tuple = tuple(my_list)
print(my_tuple)

back_to_list = list(my_tuple)
print(back_to_list)

# ✅ TODO: Convert your 'months' tuple to a list, add an extra month, then convert back.

# 🧠 BONUS CHALLENGES
# -----------------------------

# ✅ TODO: Write a function that accepts any number of arguments and returns them as a tuple.
# ✅ TODO: Write a function that takes a tuple of numbers and returns only the even ones as a new tuple.
# ✅ TODO: Given a list of tuples (name, age), sort it by age.
# ✅ TODO: From a string sentence, return a tuple of unique words sorted alphabetically.

# =============================
# ✅ YOU’VE REACHED THE END 🎉
# =============================

# You now have the most essential tools to master Python tuples.
# Practice each TODO and run this file to test results.
