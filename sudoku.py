grid = []
print("Enter the Sudoku puzzle row by row.")
print("Type 9 digits per row. Use 0 for empty boxes. Example: 530070000")

for i in range(9):
    while True:
        row = input("Row " + str(i + 1) + ": ")
        if len(row) == 9 and row.isdigit():
            grid.append([int(ch) for ch in row])
            break
        print("Please type exactly 9 digits (0-9).")

def show(grid):
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("------+-------+------")
        row = ""
        for c in range(9):
            if c % 3 == 0 and c != 0:
                row += "| "
            row += str(grid[r][c]) + " "
        print(row)

def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    start_row = row - row % 3
    start_col = col - col % 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == num:
                return False
    return True

def solve(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

print("\nUnsolved puzzle:")
show(grid)

if solve(grid):
    print("\nSolved puzzle:")
    show(grid)
else:
    print("No solution found.")