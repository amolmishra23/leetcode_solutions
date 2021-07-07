class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @functools.lru_cache(None)
        def solve(i, j):
            if j<0: return 1
            if i<0: return 0
            if s[i]==t[j]: return solve(i-1, j)+solve(i-1,j-1)
            return solve(i-1,j)
        
        return solve(len(s)-1, len(t)-1)