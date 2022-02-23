class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @functools.lru_cache(None)
        def solve(m, n):
            if m==x-1 and n==y-1: return 1
            
            if not 0<=m<x or not 0<=n<y: return 0
            
            return solve(m+1, n) + solve(m, n+1)
        
        x, y = m, n
        return solve(0,0)
            