"""
Python String Concepts - Based on Your Provided Content
======================================================
This file demonstrates the exact string concepts mentioned in your text.
"""

print("=" * 60)
print("PYTHON STRING CONCEPTS")
print("=" * 60)

# 1. BASIC STRING CONCEPT
print("\n1. BASIC STRING CONCEPT")
print("-" * 40)

# A string is a sequence of characters
# Python treats anything inside quotes as a string
# Python has no character data type so single character is a string of length 1

s = "GfG"
print(f"String s = '{s}'")
print(f"Access 2nd char: s[1] = '{s[1]}'")  # access 2nd char

s1 = s + s[0]  # update
print(f"Update string: s1 = s + s[0] = '{s1}'")  # print

print(f"s holds the value '{s}' and is defined as a string")

# 2. CREATING A STRING
print("\n2. CREATING A STRING")
print("-" * 40)

# Strings can be created using either single (') or double (") quotes
s1 = 'GfG'
s2 = "GfG"
print(f"Single quotes: s1 = '{s1}'")
print(f"Double quotes: s2 = '{s2}'")

# 3. MULTI-LINE STRINGS
print("\n3. MULTI-LINE STRINGS")
print("-" * 40)

# If we need a string to span multiple lines then we can use triple quotes (''' or """)
s = """I am Learning
Python String on GeeksforGeeks"""
print("Triple double quotes:")
print(s)

s = '''I'm a 
Geek'''
print("\nTriple single quotes:")
print(s)

# 4. ACCESSING CHARACTERS IN PYTHON STRING
print("\n4. ACCESSING CHARACTERS IN PYTHON STRING")
print("-" * 40)

# Strings are indexed starting from 0 and -1 from end
s = "GeeksforGeeks"
print(f"String: '{s}'")

# Accesses first character: 'G'
print(f"s[0] = '{s[0]}'  # Accesses first character")

# Accesses 5th character: 's'
print(f"s[4] = '{s[4]}'  # Accesses 5th character")

# Note: Accessing an index out of range will cause an IndexError
# Only integers are allowed as indices

# 5. ACCESS STRING WITH NEGATIVE INDEXING
print("\n5. ACCESS STRING WITH NEGATIVE INDEXING")
print("-" * 40)

# Python allows negative address references to access characters from back of the String
# -1 refers to the last character, -2 refers to the second last character, and so on
s = "GeeksforGeeks"

# Accesses 3rd character: 'k'
print(f"s[-10] = '{s[-10]}'  # Accesses 3rd character")

# Accesses 5th character from end: 'G'
print(f"s[-5] = '{s[-5]}'   # Accesses 5th character from end")

# 6. STRING SLICING
print("\n6. STRING SLICING")
print("-" * 40)

# Slicing is a way to extract portion of a string by specifying start and end indexes
# The syntax for slicing is string[start:end], where start is starting index and end is stopping index (excluded)
s = "GeeksforGeeks"

# Retrieves characters from index 1 to 3: 'eek'
print(f"s[1:4] = '{s[1:4]}'  # Retrieves characters from index 1 to 3")

# Retrieves characters from beginning to index 2: 'Gee'
print(f"s[:3] = '{s[:3]}'   # Retrieves characters from beginning to index 2")

# Retrieves characters from index 3 to the end: 'ksforGeeks'
print(f"s[3:] = '{s[3:]}'  # Retrieves characters from index 3 to the end")

# Reverse a string
print(f"s[::-1] = '{s[::-1]}'  # Reverse a string")

# 7. STRING IMMUTABILITY
print("\n7. STRING IMMUTABILITY")
print("-" * 40)

# Strings in Python are immutable
# This means that they cannot be changed after they are created
s = "geeksforGeeks"
print(f"Original string: '{s}'")

# Trying to change the first character raises an error
# s[0] = 'I'  # Uncommenting this line will cause a TypeError

# Instead, create a new string
s = "G" + s[1:]
print(f"Create new string: s = 'G' + s[1:] = '{s}'")

# 8. DELETING A STRING
print("\n8. DELETING A STRING")
print("-" * 40)

# In Python, it is not possible to delete individual characters from a string since strings are immutable
# However, we can delete an entire string variable using the del keyword
s = "GfG"
print(f"Before deletion: s = '{s}'")

# Deletes entire string
del s

print("String deleted using 'del s'")
# Note: After deleting the string using del and if we try to access s then it will result in a NameError

# 9. UPDATING A STRING
print("\n9. UPDATING A STRING")
print("-" * 40)

# To update a part of a string we need to create a new string since strings are immutable
s = "hello geeks"
print(f"Original string: '{s}'")

# Updating by creating a new string
s1 = "H" + s[1:]
print(f"s1 = 'H' + s[1:] = '{s1}'")

# replacing "geeks" with "GeeksforGeeks"
s2 = s.replace("geeks", "GeeksforGeeks")
print(f"s2 = s.replace('geeks', 'GeeksforGeeks') = '{s2}'")

# Explanation:
print("\nExplanation:")
print("For s1: The original string s is sliced from index 1 to end and then concatenate 'H'")
print("For s2: We used replace() method to replace 'geeks' with 'GeeksforGeeks'")

# 10. COMMON STRING METHODS
print("\n10. COMMON STRING METHODS")
print("-" * 40)

# len(): returns the total number of characters in a string
s = "GeeksforGeeks"
print(f"String: '{s}'")
print(f"len(s) = {len(s)}")

# upper() and lower() methods
s = "Hello World"
print(f"\nString: '{s}'")
print(f"s.upper() = '{s.upper()}'   # Converts all characters to uppercase")
print(f"s.lower() = '{s.lower()}'   # Converts all characters to lowercase")

# strip() and replace() methods
s = "   Gfg   "
print(f"\nString with spaces: '{s}'")
print(f"s.strip() = '{s.strip()}'    # Removes leading and trailing whitespace")

s = "Python is fun"
print(f"\nString: '{s}'")
print(f"s.replace('fun', 'awesome') = '{s.replace('fun', 'awesome')}'  # Replaces 'fun' with 'awesome'")

# 11. CONCATENATING AND REPEATING STRINGS
print("\n11. CONCATENATING AND REPEATING STRINGS")
print("-" * 40)

# Strings can be combined by using + operator
s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2
print(f"s1 = '{s1}'")
print(f"s2 = '{s2}'")
print(f"s3 = s1 + ' ' + s2 = '{s3}'")

# We can repeat a string multiple times using * operator
s = "Hello "
print(f"\nString: '{s}'")
print(f"s * 3 = '{s * 3}'")

# 12. FORMATTING STRINGS
print("\n12. FORMATTING STRINGS")
print("-" * 40)

# Using f-strings
# The simplest and most preferred way to format strings is by using f-strings
name = "Alice"
age = 22
print(f"name = '{name}', age = {age}")
print(f"f'Name: {{name}}, Age: {{age}}' = 'Name: {name}, Age: {age}'")

# Using format()
# Another way to format strings is by using format() method
s = "My name is {} and I am {} years old.".format("Alice", 22)
print(f"\nUsing format() method:")
print(f"s = '{s}'")

# 13. USING 'in' FOR STRING MEMBERSHIP TESTING
print("\n13. USING 'in' FOR STRING MEMBERSHIP TESTING")
print("-" * 40)

# The 'in' keyword checks if a particular substring is present in a string
s = "GeeksforGeeks"
print(f"String: '{s}'")
print(f"'Geeks' in s = {'Geeks' in s}")
print(f"'GfG' in s = {'GfG' in s}")

print("\n" + "=" * 60)
print("END OF PYTHON STRING CONCEPTS")
print("=" * 60)

concept="Akshay"
concept[0]="D"
print(concept)