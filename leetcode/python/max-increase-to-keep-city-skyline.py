class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        total_sum = 0
        n = len(grid)
        max_row_vals = [None] * n
        max_col_vals = [None] * n
        
        for i in range(n):
            for j in range(n):
                # loop through list and identify max vals for rows and columns
                max_row_vals[i] = max(max_row_vals[i], grid[i][j])
                max_col_vals[j] = max(max_col_vals[j], grid[i][j])
                

        for i in range(n):
            for j in range(n):
                # subtract by min val of row and column
                total_sum += min(max_row_vals[i], max_col_vals[j]) - grid[i][j]
        
        return total_sum