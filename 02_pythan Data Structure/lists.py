# ========================================================
# 🐍 PYTHON LISTS: FULL PRACTICE WORKBOOK (.py FORMAT)
# ========================================================
# This file covers all important Python list concepts with:
# - Concepts explained
# - Code examples
# - Practice tasks (marked as TODO)
# ========================================================

# 🔰 1. Introduction to Python Lists
# ----------------------------------
# Lists are ordered, mutable collections in Python.
# Syntax: list_name = [item1, item2, item3]

fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# ✅ TODO: Create a list called 'cities' with at least 5 city names.

# 📌 Accessing Elements
print(fruits[1])     # banana
print(fruits[-1])    # cherry (last element)

# ✅ TODO: Access the third city in your list.

# 🔁 Looping through a List
for fruit in fruits:
    print("I like", fruit)

# ✅ TODO: Print all your cities using a for loop.

# ➕ Adding Elements
fruits.append("orange")
fruits.insert(1, "kiwi")

# ✅ TODO: Append a new city and insert another at index 2.

# ❌ Removing Elements
fruits.remove("banana")
last = fruits.pop()   # removes last
del fruits[0]         # deletes first
# fruits.clear()      # clears all elements

# ✅ TODO: Remove any 2 cities from your list using different methods.

# 🧮 List Length
print(len(fruits))

# ✅ TODO: Print how many cities are in your list.

# 🔄 List Slicing
numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[1:5])     # [1,2,3,4]
print(numbers[:4])      # [0,1,2,3]
print(numbers[-3:])     # [4,5,6]
print(numbers[::-1])    # Reversed

# ✅ TODO: Slice your city list in 3 different ways.

# ✅ TODO: Reverse your city list using slicing.

# 🔍 Searching and Membership
print("apple" in fruits)      # True or False
print(fruits.index("kiwi"))   # Get index

# ✅ TODO: Check if a city exists in your list.

# 🧠 List Comprehensions
squares = [x ** 2 for x in range(10)]
print(squares)

# ✅ TODO: Create a list of cubes from 1 to 10.

# 🎯 Filtering with List Comprehension
nums = [1, 2, 3, 4, 5, 6]
evens = [x for x in nums if x % 2 == 0]
print(evens)

# ✅ TODO: Make a list of only cities with names longer than 5 letters.

# 🎲 Sorting and Reversing
nums.sort()            # ascending
nums.sort(reverse=True)
fruits_sorted = sorted(fruits)  # new sorted list

# ✅ TODO: Sort your cities alphabetically and then reverse the list.

# 🧩 Nested Lists
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix[1][2])   # 6

# ✅ TODO: Create a 2x3 matrix of your own and access one element.

# ➗ Splitting and Joining
sentence = "Python is awesome"
words = sentence.split()
print(words)
joined = ", ".join(words)
print(joined)

# ✅ TODO: Split a custom sentence into words and rejoin with '-' instead of space.

# 📊 List Functions
print(max(nums))
print(min(nums))
print(sum(nums))

# ✅ TODO: Find max, min, sum of a custom numeric list you create.

# 🧹 Removing Duplicates
items = [1,2,2,3,4,4,5]
unique = list(set(items))
print(unique)

# ✅ TODO: Remove duplicates from a list: [1,1,2,3,3,4,4,5]

# 🔁 Copying Lists
a = [1,2,3]
b = a.copy()
b.append(4)
print(a, b)

# ✅ TODO: Copy your cities list, change one, print both.

# 🧠 BONUS CHALLENGES (Advanced)
# -----------------------------

# ✅ TODO: Write a function to check if a list is a palindrome.
# ✅ TODO: Rotate a list right by 2 positions.
# ✅ TODO: Find common elements between two lists.
# ✅ TODO: Make a list of tuples: (city_name, length_of_name)
# ✅ TODO: From a sentence, build a list of word lengths (excluding punctuation)

# =============================
# ✅ YOU’VE REACHED THE END 🎉
# =============================

# You now have the most important tools to master Python lists.
# Practice each TODO and re-run to see results.
