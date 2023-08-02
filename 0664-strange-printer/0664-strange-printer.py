class Solution:
    def strangePrinter(self, s: str) -> int:
        @lru_cache(None)
        def solve(i, j):
            if i==j: return 1
            
            res = float("inf")
            for k in range(i, j):
                res = min(res, solve(i, k) + solve(k+1, j))
                
            return res-1 if s[i]==s[j] else res
        
        return solve(0, len(s)-1)