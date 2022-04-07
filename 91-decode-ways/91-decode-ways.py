class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        @lru_cache(None)
        def solve(idx):
            if idx>=n: return 1
            
            res, c = 0, s[idx]
            
            if int(c)>0: res += solve(idx+1)
                
            if idx+1 < n and 10<=int(s[idx:idx+2])<=26: res += solve(idx+2)
                    
            return res
        
        return solve(0)