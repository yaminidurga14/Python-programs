def is_valid(board, row, col, num):
    # Check if the number is in the row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check if the number is in the column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check if the number is in the 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try all numbers from 1 to 9
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Place the number

                        if solve_sudoku(board):  # Recursively solve the rest
                            return True

                        board[row][col] = 0  # Backtrack if not solvable

                return False  # If no number fits, return False

    return True  # Puzzle is solved


def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))


# Example usage
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

print("Sudoku Puzzle:")
print_board(sudoku_board)

if solve_sudoku(sudoku_board):
    print("\nSolved Sudoku:")
    print_board(sudoku_board)
else:
    print("No solution exists!")
