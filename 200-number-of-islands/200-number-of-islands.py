class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def mark_visited(grid, m, n, i, j):
            if not 0<=i<m or not 0<=j<n or not grid[i][j]=='1': return
            
            grid[i][j] = '2'
            
            mark_visited(grid, m, n, i-1, j)
            mark_visited(grid, m, n, i+1, j)
            mark_visited(grid, m, n, i, j-1)
            mark_visited(grid, m, n, i, j+1)
            
        m = len(grid)
        if m==0: return 0
        n = len(grid[0])
        if n==0: return 0
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    mark_visited(grid, m, n, i, j)
                    res +=1
        
        return res