# Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and Backtracking for n-queens problem or a graph coloring problem.

def is_safe(board, row, col):
    # Check if there is a queen in the same column or diagonal
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

def solve_n_queens(n):
    def backtrack(row):
        nonlocal solutions
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    board = [-1] * n
    solutions = []
    backtrack(0)
    return solutions

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "-" for cell in row))
    print()

# Usage
n = 4
solutions = solve_n_queens(n)
if solutions:
    print("Solutions found:")
    for solution in solutions:
        print_board([[1 if i == col else 0 for col in solution] for i in range(n)])
else:
    print("No solution found.")