class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def dfs(i, j):
            tmp = matrix[i][j]
            
            return 1 + max(
                dfs(i-1, j) if i-1>=0 and matrix[i-1][j]<tmp else 0,
                dfs(i+1, j) if i+1<m and matrix[i+1][j]<tmp else 0,
                dfs(i, j-1) if j-1>=0 and matrix[i][j-1]<tmp else 0,
                dfs(i, j+1) if j+1<n and matrix[i][j+1]<tmp else 0
            )   
        
        if not matrix or not matrix[0]: return 0
        m, n, res = len(matrix), len(matrix[0]), float('-inf')
        
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i,j))
                
        return res