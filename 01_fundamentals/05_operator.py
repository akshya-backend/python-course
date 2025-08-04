# -----------------------------
# 🔢 ARITHMETIC OPERATORS
# -----------------------------
a = 10
b = 3

print("a + b =", a + b)       # ➕ Addition → 13
print("a - b =", a - b)       # ➖ Subtraction → 7
print("a * b =", a * b)       # ✖ Multiplication → 30
print("a / b =", a / b)       # ➗ Division → 3.333...
print("a // b =", a // b)     # 🧹 Floor Division → 3
print("a % b =", a % b)       # 🔁 Modulus → 1
print("a ** b =", a ** b)     # 🚀 Exponentiation → 1000

# 🎯 TRICK: What is 2 ** 3 ** 2 ?
# → Right-to-left: 3**2 = 9, then 2**9 = 512

# -----------------------------
# 🧱 COMPARISON OPERATORS
# -----------------------------
print(a == b)    # False
print(a != b)    # True
print(a > b)     # True
print(a < b)     # False
print(a >= b)    # True
print(a <= b)    # False

# 🎯 TRICK: What does this return?
# print(5 == 5.0)  → True (int vs float, values match)

# -----------------------------
# 🔗 LOGICAL OPERATORS
# -----------------------------
x = True
y = False

print(x and y)     # False
print(x or y)      # True
print(not x)       # False

# 🎯 TRICK: What does this return?
# print(0 or 2 and 3) → 3 (and has higher precedence than or)

# -----------------------------
# ⚙️ BITWISE OPERATORS
# -----------------------------
p = 5     # 0101
q = 3     # 0011

print(p & q)       # 1
print(p | q)       # 7
print(p ^ q)       # 6
print(~p)          # -6 (-(p+1))
print(p << 1)      # 10
print(p >> 1)      # 2

# 🎯 TRICK: print(~True) → -2 (True = 1, ~1 = -2)

# -----------------------------
# 🖊 ASSIGNMENT OPERATORS
# -----------------------------
x = 5
x += 2      # x = x + 2 → 7
x *= 3      # x = x * 3 → 21
x //= 4     # x = x // 4 → 5
x -= 1      # x = x - 1 → 4
x %= 3      # x = x % 3 → 1

# 🎯 TRICK: What happens here?
# x = 10
# x /= 3
# print(type(x)) → <class 'float'>

# -----------------------------
# 🧠 IDENTITY OPERATORS
# -----------------------------
a = [1, 2]
b = a
c = [1, 2]

print(a is b)         # True
print(a is c)         # False
print(a is not c)     # True

# 🎯 TRICK: 'is' checks memory, not value:
# a == c → True, but a is c → False

# -----------------------------
# 🔍 MEMBERSHIP OPERATORS
# -----------------------------
list1 = [1, 2, 3]

print(2 in list1)          # True
print(5 not in list1)      # True

# 🎯 TRICK: What about this?
# 'a' in 'apple' → True

# -----------------------------
# ❓ TERNARY OPERATOR
# -----------------------------
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)              # Adult

# 🎯 TRICK: Nested ternary
# print("Even" if 4 % 2 == 0 else "Odd") → Even
# print("A" if False else "B" if True else "C") → B
