class Solution:
    def minSteps(self, n: int) -> int:
        @lru_cache(None)
        def solve(chars):
            if chars==n: return 0
            
            res = float('inf')
            
            # if we have 10 chars on screen, and need 100 chars total. 
            # We will only do 10*10=100 max
            for paste in range(1, n//chars+1):
                if chars + paste*chars > n: break
                res = min(res, paste+solve(chars+paste*chars))
                
            # (plus one is for copying once)
            return res+1
        
        return solve(1)