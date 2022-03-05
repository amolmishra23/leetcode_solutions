class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m==0: return grid
        n = len(grid[0])
        max_row_vals = [None]*m
        max_col_vals = [None]*n
        result = 0
        
        for i in range(m):
            max_row_vals[i] = max(grid[i])
        
        transpose = list(zip(*grid))
        for j in range(n):
            max_col_vals[j] = max(transpose[j])
        
        for i in range(m):
            for j in range(n):
                result += min(max_row_vals[i], max_col_vals[j])-grid[i][j]
                
        return result