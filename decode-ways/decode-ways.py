class Solution:
    def numDecodings(self, s: str) -> int:
        @functools.lru_cache(None)
        def solve(s, i):
            if i>=len(s): return 1
            
            res, c = 0, s[i]
            
            if int(c)>0: res += solve(s, i+1)
                
            if i+1<len(s) and 10<=int(s[i:i+2])<=26: res+=solve(s, i+2)
                
            return res
        
        return solve(s, 0)