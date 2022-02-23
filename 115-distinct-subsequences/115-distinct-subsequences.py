class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @functools.lru_cache(None)
        def solve(i, j):
          if j==len(t): return 1
          if i==len(s): return 0
          
          if s[i]==t[j]:
            return solve(i+1,j+1)+solve(i+1,j)
          
          return solve(i+1,j)
        
        return solve(0,0)