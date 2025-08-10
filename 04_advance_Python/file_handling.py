# ============================================
# 📂 File Handling in Python — From 0 to Advanced
# ============================================

# Python provides built-in functions for reading, writing, and manipulating files.
# Files can be of different types: text (.txt, .csv) or binary (.jpg, .mp4, etc.)

# --------------------------------------------
# 1. Opening a file
# --------------------------------------------
# Syntax: open(filename, mode)
# Modes:
#   "r"  → Read (default, file must exist)
#   "w"  → Write (creates new file or overwrites existing)
#   "a"  → Append (adds data to the end of file)
#   "x"  → Create (error if file exists)
#   "rb" → Read binary
#   "wb" → Write binary

# Let's create and write to a file
file = open("example.txt", "w")  # Open in write mode
file.write("Hello, World!\n")
file.write("This is the first line of the file.\n")
file.close()

# --------------------------------------------
# 2. Reading from a file
# --------------------------------------------
file = open("example.txt", "r")  # Read mode
content = file.read()  # Reads entire file
print("Full content:\n", content)
file.close()

# --------------------------------------------
# 3. Reading line by line
# --------------------------------------------
file = open("example.txt", "r")
print("\nReading line by line:")
for line in file:
    print(line.strip())  # strip() removes \n
file.close()

# --------------------------------------------
# 4. Reading specific number of characters
# --------------------------------------------
file = open("example.txt", "r")
first_5_chars = file.read(5)  # Reads first 5 characters
print("\nFirst 5 characters:", first_5_chars)
file.close()

# --------------------------------------------
# 5. Using 'with' statement (Best Practice)
# --------------------------------------------
# 'with' automatically closes the file after use
with open("example.txt", "r") as file:
    print("\nUsing 'with':")
    print(file.read())

# --------------------------------------------
# 6. Appending to a file
# --------------------------------------------
with open("example.txt", "a") as file:
    file.write("Appending a new line!\n")

# --------------------------------------------
# 7. Writing multiple lines at once
# --------------------------------------------
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("multilines.txt", "w") as file:
    file.writelines(lines)  # Writes a list of strings

# --------------------------------------------
# 8. Reading all lines into a list
# --------------------------------------------
with open("multilines.txt", "r") as file:
    all_lines = file.readlines()
print("\nAll lines from multilines.txt:", all_lines)

# --------------------------------------------
# 9. Working with binary files (images, videos, etc.)
# --------------------------------------------
# Copying a binary file
with open("source_image.jpg", "rb") as src_file:
    with open("copy_image.jpg", "wb") as dest_file:
        dest_file.write(src_file.read())

# --------------------------------------------
# 10. File pointer handling: seek() & tell()
# --------------------------------------------
with open("example.txt", "r") as file:
    print("\nCurrent position:", file.tell())  # tell() gives current pointer position
    file.seek(7)  # Move pointer to the 8th character (index starts at 0)
    print("After seek(7):", file.read())

# --------------------------------------------
# 11. Error handling in file operations
# --------------------------------------------
try:
    with open("non_existent.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("\nError: File not found!")
except PermissionError:
    print("Error: No permission to read the file.")
except Exception as e:
    print("Unexpected error:", e)

# --------------------------------------------
# 12. OS module for file handling
# --------------------------------------------
import os

# Check if file exists
if os.path.exists("example.txt"):
    print("\nexample.txt exists!")
else:
    print("example.txt not found!")

# Rename a file
os.rename("multilines.txt", "renamed_file.txt")

# Delete a file
if os.path.exists("renamed_file.txt"):
    os.remove("renamed_file.txt")

# Create a directory
if not os.path.exists("my_folder"):
    os.mkdir("my_folder")

# --------------------------------------------
# 13. Advanced: Reading large files efficiently
# --------------------------------------------
# Instead of reading the whole file into memory (bad for huge files),
# read it in chunks.
with open("example.txt", "r") as file:
    while True:
        chunk = file.read(10)  # Read 10 characters at a time
        if not chunk:
            break
        print("Chunk:", chunk)

# --------------------------------------------
# 14. CSV file handling
# --------------------------------------------
import csv

# Writing CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "New York"])
    writer.writerow(["Bob", 30, "London"])

# Reading CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print("CSV Row:", row)

# --------------------------------------------
# 15. JSON file handling
# --------------------------------------------
import json

# Writing JSON
data = {"name": "Alice", "age": 25, "city": "New York"}
with open("data.json", "w") as file:
    json.dump(data, file)

# Reading JSON
with open("data.json", "r") as file:
    loaded_data = json.load(file)
print("\nJSON content:", loaded_data)

# ============================================
# ✅ This file covers:
# - Basic read/write/append
# - Reading modes & binary handling
# - File pointers
# - Error handling
# - OS file management
# - Efficient file reading
# - CSV & JSON handling
# ============================================
