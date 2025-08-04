# ========================================================
# 🐍 PYTHON SETS: FULL PRACTICE WORKBOOK (.py FILE)
# ========================================================
# Sets are unordered collections of unique elements.
# This workbook includes:
# - Concept explanations
# - Code examples
# - Hands-on TODOs
# ========================================================

# 🔰 1. Introduction to Sets
# ----------------------------
# Sets are like lists, but only hold **unique values**, and are **unordered**.

fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)  # Duplicates removed → {'apple', 'banana', 'cherry'}

# ✅ TODO: Create a set of your 5 favorite books (some repeated to test uniqueness)

# 📌 Key Properties:
# - Unordered → No indexing
# - No duplicates
# - Mutable (you can add/remove)

# 🔄 Adding Elements
fruits.add("mango")
fruits.update(["kiwi", "grapes"])
print(fruits)

# ✅ TODO: Add 2 more books to your book set using `add()` and `update()`

# ❌ Removing Elements
fruits.remove("banana")   # Raises error if not present
fruits.discard("pineapple")  # Safe, no error
print(fruits)

# ✅ TODO: Safely remove one book and try removing a non-existing one using discard()

# 🧪 Checking Membership
print("apple" in fruits)
print("papaya" not in fruits)

# ✅ TODO: Check if one book is in your book set

# 🔁 Looping through a Set
for item in fruits:
    print(item)

# ✅ TODO: Loop through your book set and print each with “I like reading ...”

# 🧮 Set Operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)           # {1,2,3,4,5,6}
print("Intersection:", A & B)   # {3,4}
print("Difference A-B:", A - B) # {1,2}
print("Symmetric Difference:", A ^ B)  # {1,2,5,6}

# ✅ TODO: Create two number sets and print all 4 basic set operations.

# 🎯 Set Comparisons
C = {1, 2}
D = {1, 2, 3}

print(C.issubset(D))       # True
print(D.issuperset(C))     # True
print(C.isdisjoint({5}))   # True

# ✅ TODO: Check if one of your sets is a subset or superset of another.

# 🧠 Set Comprehension
squares = {x**2 for x in range(6)}
print(squares)

# ✅ TODO: Create a set of all even numbers from 1 to 20 using set comprehension.

# 🔄 Converting Between Set, List, and Tuple
nums_list = [1, 2, 2, 3, 4, 4]
unique_nums = set(nums_list)
print(unique_nums)

nums_back = list(unique_nums)
print(nums_back)

# ✅ TODO: Convert your book set to a list, add a new book, convert back to set.

# 🧹 Clearing & Copying
A = {1, 2, 3}
B = A.copy()
A.clear()

print("A:", A)
print("B:", B)

# ✅ TODO: Copy your set, clear the original, print both

# 📚 Real World Example
sentence = "python is great and python is easy"
words = set(sentence.split())
print(words)

# ✅ TODO: Take a custom sentence and print all unique words using a set.

# 🎲 Frozen Sets (Immutable Sets)
fset = frozenset([1, 2, 3, 3, 4])
print(fset)

# ✅ TODO: Create a frozenset of your favorite numbers and try to add an element (observe the error)

# 🧠 BONUS CHALLENGES
# -----------------------

# ✅ TODO: Given two sets of registered and attended students, find absentees.
# ✅ TODO: Write a function that removes all duplicates from a list using sets.
# ✅ TODO: From two word sets, find common and unique letters.
# ✅ TODO: Build a set from all vowels present in a sentence.
# ✅ TODO: Check if a list has any duplicate elements using sets.

# =============================
# ✅ YOU’VE MASTERED SETS 🎉
# =============================

# Run this file regularly.
# Solve each TODO and rerun to test your answers.
