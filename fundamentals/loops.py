# ============================================
# 🔁 PYTHON LOOPS: Complete Beginner Guide
# ============================================

# 🔍 What is a Loop?
# A loop allows you to repeat a block of code multiple times.
# Python supports two main types of loops:
#   1. for loop – used to iterate over a sequence (like list, tuple, string, dictionary, set)
#   2. while loop – keeps running as long as a condition is True

# ============================================
# ✅ FOR LOOP – Syntax:
# for variable in iterable:
#     # block of code
# ============================================

print("👉 FOR LOOP with different data types\n")

# 1️⃣ STRING
text = "loop"
for char in text:
    print(char)

# 2️⃣ LIST
numbers = [10, 20, 30]
for num in numbers:
    print(num)

# 3️⃣ TUPLE
coordinates = (1, 2, 3)
for point in coordinates:
    print(point)

# 4️⃣ SET (unordered, unique)
unique_numbers = {100, 200, 300}
for num in unique_numbers:
    print(num)

# 5️⃣ DICTIONARY (looping keys)
person = {"name": "Alice", "age": 30}
for key in person:
    print(f"{key} -> {person[key]}")

# 6️⃣ DICTIONARY (key-value pairs)
for key, value in person.items():
    print(f"{key} = {value}")

# 7️⃣ RANGE object (generates sequence of numbers)
for i in range(3):
    print(i)

# 8️⃣ ENUMERATE (get index + value)
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(index, ":", color)

# 9️⃣ LIST OF DICTS
data = [{"id": 1}, {"id": 2}, {"id": 3}]
for item in data:
    print(item["id"])

# 🔟 BOOLEAN (Not Iterable)
try:
    for b in True:
        print(b)
except TypeError as e:
    print("❌ Error:", e)

# 1️⃣1️⃣ NONE (Not Iterable)
try:
    for n in None:
        print(n)
except TypeError as e:
    print("❌ Error:", e)


# ============================================
# ✅ WHILE LOOP – Syntax:
# while condition:
#     # block of code
# ============================================

print("\n👉 WHILE LOOP demo")

# 1️⃣ Basic while loop
counter = 0
while counter < 3:
    print("Counter:", counter)
    counter += 1

# 2️⃣ Infinite loop with break
i = 0
while True:
    if i == 2:
        break
    print("Breaking at i =", i)
    i += 1


# ============================================
# 🎯 5 TRICKY LOOP QUESTIONS (INTERVIEW STYLE)
# ============================================

print("\n🎯 Trick Q1: Loop with mixed data types")
mixed = [123, "abc", [1,2], {"x": 5}, (1,2), {1,2}]
for item in mixed:
    print(f"{item} --> type: {type(item)}")

print("\n🎯 Trick Q2: Looping dict directly vs items()")
d = {"x": 1, "y": 2}
for k in d:
    print("Key only:", k)
for k, v in d.items():
    print("Key-Value:", k, v)

print("\n🎯 Trick Q3: Looping over string with condition")
text = "python"
for char in text:
    if char in "aeiou":
        print(char, "is a vowel")
    else:
        print(char, "is a consonant")

print("\n🎯 Trick Q4: Using range with step (reverse)")
for i in range(10, 0, -2):
    print("Countdown:", i)

print("\n🎯 Trick Q5: Nested loop on 2D list (Matrix)")
matrix = [[1, 2], [3, 4], [5, 6]]
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()

# ============================================
# 📌 Summary
# - Use `for` for finite sequences like strings, lists, dicts.
# - Use `while` when you need conditional repeating.
# - Be careful when looping over non-iterables (bool, None).
# - Use range(), enumerate(), and dict.items() for power!
# ============================================
