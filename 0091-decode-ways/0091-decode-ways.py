class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def solve(i):
            # we have reached end of string (success case)
            if i>=len(s): return 1
            res = 0
            
            # single digit rule being it should be non-zero
            if int(s[i])>0:
                res += solve(i+1)
                
            # double digit rule being it should be between 10-26. 
            if i+1<len(s) and 10<=int(s[i:i+2])<=26:
                res += solve(i+2)
                
            return res
        
        return solve(0)