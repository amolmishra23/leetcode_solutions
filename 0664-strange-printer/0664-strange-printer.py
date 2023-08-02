class Solution:
    def strangePrinter(self, s: str) -> int:
        @lru_cache(None)
        def solve(i, j):
            # for 1 character string, we need 1 attempt for sure. 
            if i==j: return 1
            
            res = float("inf")
            # same like matrix chain multiplication we break at every point
            for k in range(i, j):
                res = min(res, solve(i, k) + solve(k+1, j))
                
            # subtract 1 because if 1st and last char are same. 1 try less needed.
            # to understand better try the examples: aa, aaba, aabab etc
            return res-1 if s[i]==s[j] else res
        
        return solve(0, len(s)-1)