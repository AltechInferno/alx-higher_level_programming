#!/usr/bin/python3
import sys

# Function to check if a queen can be placed at the given position
def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check if there is a queen in the upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    i, j = row, col
    while i >= 0 and j < N:
        if board[i] == j:
            return False
        i -= 1
        j += 1

    # It is safe to place a queen at the given position
    return True

# Function to solve the N Queens problem recursively
def solve_nqueens(board, row):
    # Base case: All queens have been placed, add the solution to the result
    if row == N:
        result.append([[i, board[i]] for i in range(N)])
        return

    # Try placing the queen in each column of the current row
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1)

# Check if the program is called with the correct number of arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Get the value of N from command line argument
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Check if N is greater or equal to 4
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Create an empty board of size N x N
board = [0] * N

# List to store the solutions
result = []

# Solve the N Queens problem
solve_nqueens(board, 0)

# Print the solutions
for solution in result:
    print(solution)

