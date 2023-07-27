def is_valid(board, row, col, num):
           # Check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def solve_sudoku(board):
    row, col = find_empty_cell(board)

    if row is None and col is None:
        return True  # No empty cell left, the puzzle is solved

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            # If the current number doesn't lead to a solution, backtrack
            board[row][col] = 0

    return False

if __name__ == "__main__":
    # Example Sudoku puzzle (0 represents empty cells)
    sudoku_board = [
        [0, 0, 6, 3, 0, 7, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 5],
        [1, 0, 0, 0, 0, 6, 0, 8, 2],
        [2, 0, 5, 0, 3, 0, 1, 0, 6],
        [0, 0, 0, 2, 0, 0, 3, 0, 0],
        [9, 0, 0, 0, 7, 0, 0, 0, 4],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 1, 0, 9, 0, 4, 0]
    ]

    if solve_sudoku(sudoku_board):
        print("Sudoku solved:")
        for row in sudoku_board:
            print(row)
    else:
        print("No solution exists for the given Sudoku puzzle.")
