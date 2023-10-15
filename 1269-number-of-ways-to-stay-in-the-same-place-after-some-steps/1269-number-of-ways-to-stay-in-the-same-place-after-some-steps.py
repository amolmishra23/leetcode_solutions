class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = lambda x: x%((10**9)+7)
        
        @lru_cache(None)
        def dp(curr, rem):
            if curr>=arrLen or curr<0: return 0
            if rem==0: return curr==0
            return MOD(sum(MOD(dp(curr+i, rem-1)) for i in range(-1,2)))
            
        return dp(0, steps)