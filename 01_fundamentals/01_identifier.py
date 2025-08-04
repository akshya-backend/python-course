# beginner_identifiers_and_tricky_questions.py

"""
===========================
✅ WHAT IS AN IDENTIFIER?
===========================

An identifier is the **name** you give to things in Python like:
- variables
- functions
- classes
- modules

➡️ Example:
    name = "Alice"      # 'name' is an identifier
    def greet(): ...    # 'greet' is an identifier
    class Student: ...  # 'Student' is an identifier

"""

# -------------------------------
# 📌 BASIC RULES FOR IDENTIFIERS:
# -------------------------------
# 1. Must start with a letter (A-Z or a-z) or underscore (_)
# 2. Can include letters, digits (0-9), and underscores
# 3. Cannot start with a number
# 4. Cannot be a Python keyword (like `class`, `for`, `if`, etc.)
# 5. Are case-sensitive (Name ≠ name)

# ---------------------------------------
# 🔥 TRICKY QUESTION 1: Keyword as Name
# ---------------------------------------

# ❌ This will cause an error because 'class' is a reserved word:
# class = 5
# print(class)

# ✅ Correct way:
class_ = 5
print("Q1 Output:", class_)  # Output: 5


# ---------------------------------------
# 🔥 TRICKY QUESTION 2: Starts with Number
# ---------------------------------------

# ❌ This will cause an error:
# 1name = "Python"

# ✅ Correct way:
name1 = "Python"
print("Q2 Output:", name1)  # Output: Python
