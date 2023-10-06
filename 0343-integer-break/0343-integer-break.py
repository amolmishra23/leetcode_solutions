class Solution:
    def integerBreak(self, n: int) -> int:        
        @lru_cache(None)
        def dp(num):
            if num <= 1: return 1
            
            res = 0
            
            for i in range(1, num):
                # Because in case of 4. We can split it as 2,2 => 2*2 => 4. 
                # Or as 2,1,1 => 2*1*1 = 2
                # hence to account both the cases we consider i*(num-i)
                # or 2nd case being i*dp(num-i)
                res = max(res, i*(num-i), i*dp(num-i))
                
            return res
        
        return dp(n)