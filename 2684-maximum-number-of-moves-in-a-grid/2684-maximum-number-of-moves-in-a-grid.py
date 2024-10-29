class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0,1), (1,1), (-1,1)]
        
        @lru_cache(None)
        def dfs(i, j):
            res = 0
            
            for x, y in dirs:
                ni, nj = i+x, j+y
                if 0<=ni<m and 0<=nj<n and grid[ni][nj] > grid[i][j]:
                    res = max(res, 1+dfs(ni, nj))
                    
            return res
            
        return max(dfs(i, 0) for i in range(m))