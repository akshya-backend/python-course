# ========================================================
# 🐍 PYTHON DICTIONARIES: FULL PRACTICE WORKBOOK (.py FILE)
# ========================================================
# Dictionaries are unordered, mutable key-value pairs in Python.
# This workbook includes:
# - Explanations
# - Code examples
# - TODOs for you to practice after each concept
# ========================================================

# 🔰 1. Introduction to Dictionaries
# ----------------------------------
# A dictionary maps unique keys to values.
# Syntax: dict_name = {key1: value1, key2: value2, ...}

person = {"name": "Alice", "age": 25, "city": "Delhi"}
print(person)

# ✅ TODO: Create a dictionary of your own profile (name, age, hobby, city).

# 🔍 Accessing Values
print(person["name"])       # Alice

# ✅ TODO: Print your hobby and city from your dictionary.

# 🧩 Adding and Updating Keys
person["email"] = "alice@example.com"  # Add
person["age"] = 26                     # Update
print(person)

# ✅ TODO: Add 'phone' and update 'city' in your dictionary.

# ❌ Removing Keys
person.pop("email")
del person["city"]

# ✅ TODO: Remove one key from your dictionary using pop().

# 🧪 Key Existence
print("name" in person)    # True
print("gender" in person)  # False

# ✅ TODO: Check if 'age' and 'country' exist in your dictionary.

# 🔁 Looping Through Dictionaries
for key in person:
    print(key, "=>", person[key])

# ✅ TODO: Loop through your dictionary and print each key and value.

# 🧾 Dictionary Methods
print(person.keys())     # dict_keys(['name', 'age'])
print(person.values())   # dict_values(['Alice', 26])
print(person.items())    # dict_items([('name', 'Alice'), ('age', 26)])

# ✅ TODO: Print all values and items of your dictionary.

# 🧠 Dictionary Comprehension
squares = {x: x ** 2 for x in range(5)}
print(squares)

# ✅ TODO: Create a dictionary mapping numbers 1–5 to their cubes.

# 🎯 Nested Dictionaries
students = {
    "john": {"age": 22, "grade": "A"},
    "emma": {"age": 21, "grade": "B"}
}
print(students["john"]["grade"])

# ✅ TODO: Create a dictionary of 2 books with inner keys: author, year.

# 🔄 Merging Dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = {**d1, **d2}
print(merged)  # {'a': 1, 'b': 3, 'c': 4}

# ✅ TODO: Merge two dictionaries of your choice (can overwrite a key).

# ⚙️ Using `get()` and `setdefault()`
print(person.get("name"))          # Alice
print(person.get("salary", 0))     # 0 (default)

person.setdefault("city", "Unknown")
print(person)

# ✅ TODO: Use get() to access a non-existing key with a default value.

# 🧹 Clearing and Copying
person_copy = person.copy()
person.clear()
print(person)         # {}
print(person_copy)    # still has values

# ✅ TODO: Copy your dictionary, clear the original, then print both.

# 💡 Dictionary from Two Lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined = dict(zip(keys, values))
print(combined)

# ✅ TODO: Make two lists: subjects and marks, then zip into a dictionary.

# 🔢 Counting with Dictionary
grades = ["A", "B", "A", "C", "B", "A"]
grade_count = {}
for grade in grades:
    grade_count[grade] = grade_count.get(grade, 0) + 1
print(grade_count)

# ✅ TODO: Count how many times each letter appears in a word.

# 📊 Dictionary Sorting (by keys or values)
data = {"math": 90, "english": 80, "science": 95}
sorted_by_key = dict(sorted(data.items()))
sorted_by_value = dict(sorted(data.items(), key=lambda x: x[1]))

print("By Key:", sorted_by_key)
print("By Value:", sorted_by_value)

# ✅ TODO: Sort a dictionary of your own by keys and by values.

# 📚 Practice Scenarios
# -----------------------

# ✅ TODO: Create a phonebook using a dictionary (name → phone).
# ✅ TODO: Make a product-price dictionary and allow user to input product name to get price.
# ✅ TODO: Convert a sentence into a frequency dictionary of words.
# ✅ TODO: Find the highest and lowest value in a dictionary.

# 🧠 BONUS CHALLENGES
# -----------------------

# ✅ TODO: Write a function that returns the key with the highest value in a dictionary.
# ✅ TODO: Given a nested dictionary of students, return average grade.
# ✅ TODO: Create a dictionary where keys are words, and values are number of vowels in them.
# ✅ TODO: From a list of tuples (name, score), convert into a dictionary and filter only those > 80.

# =============================
# ✅ YOU’VE MASTERED DICTIONARIES 🎉
# =============================

# Revisit this file often. Complete the TODOs. Create variations.
# This is how you deeply learn and retain Python dictionary skills!
