class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        @lru_cache(None)
        def dfs(r, c):
            if r == m or c==n or matrix[r][c]==0:
                return 0
            
            return 1 + min(dfs(r+1, c), dfs(r, c+1), dfs(r+1, c+1))
        
        res = 0
        for r in range(m):
            for c in range(n):
                res += dfs(r, c)
                
        return res