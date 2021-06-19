class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j):
            if not 0<=i<len(grid) or not 0<=j<len(grid[0]): return 0
            
            if grid[i][j] in (0,2): return 0
            
            grid[i][j] = 2
            
            return 1+dfs(grid, i+1, j)+dfs(grid, i-1, j)+dfs(grid, i, j+1)+dfs(grid, i, j-1)
        
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    res=max(res, dfs(grid, i, j))
                    
        return res