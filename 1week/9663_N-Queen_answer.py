def is_safe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def count_n_queens_solutions(N):
    # Initialize the board
    board = [[0] * N for _ in range(N)]
    count = [0]  # Using a list to allow modifications inside nested function

    # Helper function to count solutions
    def solve_n_queens_util(board, col, N):
        # Base case: If all queens are placed then increment count by 1
        if col >= N:
            count[0] += 1
            return

        # Consider this column and try placing this queen in all rows one by one
        for i in range(N):
            if is_safe(board, i, col, N):
                board[i][col] = 1

                # Recur to place rest of the queens
                solve_n_queens_util(board, col + 1, N)

                # Backtrack and remove queen from board[i][col]
                board[i][col] = 0

    # Solve the problem starting from the 0th column
    solve_n_queens_util(board, 0, N)
    return count[0]

# Example usage:
N = int(input())
print(count_n_queens_solutions(N))