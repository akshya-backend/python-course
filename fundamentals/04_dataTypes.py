# -------------------- NUMERIC DATA TYPES --------------------
print("\n# NUMERIC TYPES")
a = 10
print(a, type(a))  # int

b = 3.14
print(b, type(b))  # float

c = 2 + 3j
print(c, type(c))  # complex

# Tricky Questions
print("\n# Numeric Type Tricks")
x = 10 + 3.5
print(x, type(x))  # float

z = 0 + 5j
print(z.real, z.imag)

print(int(5.9))  # 5

print(0.1 + 0.2 == 0.3)  # False due to float precision

print(type(3 + 4.0))  # float

# -------------------- STRING DATA TYPE --------------------
print("\n# STRING TYPE")
s = "Hello Python"
print(s[1])
print(s[-1])
print(type(s))

# Tricky Questions
print("\n# String Type Tricks")
s = "abc"
try:
    s[0] = "A"
except Exception as e:
    print("Error:", e)

s = "python"
print(s[1:4])
print(s[-2])

s = '''Line1
Line2'''
print(s)

print("ha" * 3)

# -------------------- LIST DATA TYPE --------------------
print("\n# LIST TYPE")
fruits = ["apple", "banana", "orange"]
fruits.append("grape")
fruits.remove("orange")
print(fruits)

# Tricky Questions
print("\n# List Type Tricks")
a = [1, 2, 3]
a[1] = 100
print(a)

b = [1, "two", [3, 4]]
print(b[2][0])

print(b[-1])

lst = [1, 2]
lst.append([3, 4])
print(lst)

lst = [1, 2]
lst.extend([3, 4])
print(lst)

print([x**2 for x in range(3)])

# -------------------- TUPLE DATA TYPE --------------------
print("\n# TUPLE TYPE")
coordinates = (3, 5)
print("X:", coordinates[0])
print("Y:", coordinates[1])

# Tricky Questions
print("\n# Tuple Type Tricks")
t = (1, 2, 3)
try:
    t[0] = 10
except Exception as e:
    print("Error:", e)

t1 = (5)
print(type(t1))  # int

t2 = (5,)
print(type(t2))  # tuple

t = ([1, 2], 3)
t[0].append(3)
print(t)

a = 1, 2
print(type(a))

x, y = a
print(x, y)

t = (1, (2, 3))
print(t[1][0])

# -------------------- BOOLEAN DATA TYPE --------------------
print("\n# BOOLEAN TYPE")
print(type(True))
print(type(False))

# Tricky Questions
print("\n# Boolean Type Tricks")
try:
    print(type(true))
except Exception as e:
    print("Error:", e)

print(bool(0))  # False
print(bool(1))  # True

print(bool("False"))  # True

print(bool([]))  # False

print(5 > 3)
print(type(5 > 3))

# -------------------- SET DATA TYPE --------------------
print("\n# SET TYPE")
s = set(["apple", "banana", "apple"])
print(s)

# Tricky Questions
print("\n# Set Type Tricks")
s = set([1, 2, 3])
try:
    print(s[0])
except Exception as e:
    print("Error:", e)

s.add(4)
print(s)

s.update([5, 6])
print(s)

s.remove(5)
try:
    s.remove(10)
except Exception as e:
    print("Error:", e)

s.discard(10)  # no error

print(2 in s)

s = set("geeks")
print(s)

# -------------------- DICTIONARY DATA TYPE --------------------
print("\n# DICTIONARY TYPE")
d = {"name": "Alice", "age": 25}
print(d["name"])
print(d.get("age"))

# Tricky Questions
print("\n# Dictionary Type Tricks")
d = {"x": 1, "x": 2}
print(d)

try:
    d = {[1, 2]: "value"}  # ❌ list is unhashable
except Exception as e:
    print("Error:", e)

d = {1: "a", "1": "b"}
print(d[1])     # a
print(d["1"])   # b

d = {"a": 1, "b": 2}
for k in d:
    print(f"{k}: {d[k]}")

print("name" in d)


# Pass by Reference and Pass by Value
# One important thing to note is, in Python every variable name is a reference. When we pass a variable to a function Python, a new reference to the object is created.
# Parameter passing in Python is the same as reference passing in Java.
# Here x is a new reference to same list lst
def myFun(x):
    x[0] = 20

# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)  # Output: [20, 11, 12, 13, 14, 1
print(lst)

# Recursive Functions in Python
# Recursion in Python refers to when a function calls itself. There are many instances when you have to build a recursive function to solve Mathematical and Recursive Problems.

# Using a recursive function should be done with caution, as a recursive function can become like a non-terminating loop. It is better to check your exit statement while creating a recursive function.

def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
      
print(factorial(4))