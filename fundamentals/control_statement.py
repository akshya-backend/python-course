# -------------------------
# CONDITIONAL STATEMENT BASICS
# -------------------------

print("=== 1. IF Statement ===")
age = 20
if age >= 18:
    print("Eligible to vote.")

print("\n=== 2. Short Hand IF ===")
age = 19
if age > 18: print("Eligible to Vote.")

print("\n=== 3. IF-ELSE Statement ===")
age = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")

print("\n=== 4. Short Hand IF-ELSE (Ternary) ===")
marks = 45
res = "Pass" if marks >= 40 else "Fail"
print(f"Result: {res}")

print("\n=== 5. IF-ELIF-ELSE Statement ===")
age = 25
if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

print("\n=== 6. Nested IF-ELSE ===")
age = 70
is_member = True
if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")

print("\n=== 7. Ternary Expression Again ===")
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

print("\n=== 8. MATCH-CASE ===")
number = 2
match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")

# -------------------------
# TRICKY INTERVIEW QUESTIONS (With Explanation)
# -------------------------

print("\n=== Trick 1: Understanding indentation ===")
x = 10
if x > 5:
    print("Greater than 5")
    print("Still inside if")  # Watch indentation
print("Outside if")

print("\n=== Trick 2: Multiple conditions on one line ===")
a = 5
b = 10
if a < 10 and b > 5: print("Both conditions true")  # One-liner condition

print("\n=== Trick 3: Elif won't check further if one is True ===")
num = 15
if num > 10:
    print("Greater than 10")
elif num > 5:
    print("Greater than 5")  # This is skipped
else:
    print("5 or less")

print("\n=== Trick 4: Ternary nesting ===")
age = 16
msg = "Adult" if age >= 18 else ("Teen" if age >= 13 else "Child")
print("Age category:", msg)

print("\n=== Trick 5: Match-case with multiple patterns ===")
command = "start"
match command:
    case "run" | "start":
        print("Starting the engine")
    case "stop":
        print("Stopping")
    case _:
        print("Unknown command")
