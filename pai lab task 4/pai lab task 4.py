def solve_n_queens(n):
    def backtrack(row, cols, diag1, diag2):
        if row == n:
            # All queens are placed successfully
            return 1
        
        count = 0
        # Iterate through each column
        for col in range(n):
            # Check if the column and diagonals are free
            if (cols & (1 << col)) == 0 and (diag1 & (1 << (row - col + n - 1))) == 0 and (diag2 & (1 << (row + col))) == 0:
                # Place the queen and mark the column and diagonals as occupied
                count += backtrack(row + 1, cols | (1 << col), diag1 | (1 << (row - col + n - 1)), diag2 | (1 << (row + col)))
        
        return count

    return backtrack(0, 0, 0, 0)

# Example usage
n = 8  # Change this value for different sizes of the board
solution_count = solve_n_queens(n)
print(f"Number of solutions for {n}-Queens: {solution_count}")