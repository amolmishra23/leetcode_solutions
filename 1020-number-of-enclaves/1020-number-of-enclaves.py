class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        def dfs(i, j):
            grid[i][j]=0
            for m, n in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0<=m<r and 0<=n<c and grid[m][n] == 1:
                    dfs(m, n)
        
        for i in [0, r-1]:
            for j in range(c):
                if grid[i][j]==1: dfs(i, j)
                    
        for i in range(r):
            for j in [0, c-1]:
                if grid[i][j]==1: dfs(i, j)
                    
        res = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1: res+=1
                    
        return res