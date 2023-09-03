class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def solve(x, y):
            if x==m-1 and y==n-1: return 1
            
            if not 0<=x<m or not 0<=y<n: return 0
            
            return solve(x+1, y) + solve(x, y+1)
        
        return solve(0,0)