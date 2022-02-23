class Solution:
    def minCut(self, s: str) -> int:
        @lru_cache(None)
        def is_pal(l,r):
          if l>=r: return True
          if s[l]!=s[r]: return False
          return is_pal(l+1,r-1)
        
        @lru_cache(None)
        def solve(i):
          if i==len(s): return 0
          
          ans = float('inf')
          for j in range(i, len(s)):
            if is_pal(i, j):
              ans = min(ans, solve(j+1)+1)
              
          return ans
        
        return solve(0)-1