# 🧩 4x4 Sudoku Solver using Backtracking
# ----------------------------------------
# Rules:
# 1. Each row must contain numbers 1 to 4 without repetition.
# 2. Each column must contain numbers 1 to 4 without repetition.
# 3. Each 2x2 box must contain numbers 1 to 4 without repetition.

# ✅ Step 1: Sample board with 0 meaning empty cells
board = [
    [1, 0, 0, 4],
    [0, 0, 1, 0],
    [0, 4, 0, 0],
    [2, 0, 0, 3]
]

# ----------------------------------------
# Function to print the Sudoku board
def print_board(b):
    for row in b:
        print(row)
    print()

# ----------------------------------------
# Function to find the next empty cell
def find_empty(b):
    for i in range(4):  # row
        for j in range(4):  # column
            if b[i][j] == 0:
                return (i, j)  # row, column
    return None

# ----------------------------------------
# Check if placing num in position (row, col) is valid
def is_valid(b, num, pos):
    row, col = pos

    # Check row
    if num in b[row]:
        return False

    # Check column
    for i in range(4):
        if b[i][col] == num:
            return False

    # Check 2x2 box
    box_x = col // 2
    box_y = row // 2
    for i in range(box_y * 2, box_y * 2 + 2):
        for j in range(box_x * 2, box_x * 2 + 2):
            if b[i][j] == num:
                return False

    return True

# ----------------------------------------
# Backtracking Sudoku Solver
def solve(b):
    empty = find_empty(b)
    if not empty:
        return True  # No empty space → puzzle solved
    row, col = empty

    for num in range(1, 5):  # Try numbers 1 to 4
        if is_valid(b, num, (row, col)):
            b[row][col] = num  # Place number

            if solve(b):  # Continue recursively
                return True

            b[row][col] = 0  # Undo and try next number (Backtrack)

    return False

# ----------------------------------------
print("🔢 Original Board:")
print_board(board)

if solve(board):
    print("✅ Solved Board:")
    print_board(board)
else:
    print("❌ No solution found.")
