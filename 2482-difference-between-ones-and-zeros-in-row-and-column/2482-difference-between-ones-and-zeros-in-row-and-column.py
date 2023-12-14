class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        row_ones, col_ones = list(map(sum, grid)), list(map(sum, zip(*grid)))        
        solve = lambda i,j: row_ones[i]+col_ones[j]-(m-row_ones[i])-(n-col_ones[j])
        return [[solve(i, j) for j in range(n)] for i in range(m)]