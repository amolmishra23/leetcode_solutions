class Solution:
    def countVowelStrings(self, n: int) -> int:
        @lru_cache(None)
        def dp(n, i):
            # n denotes number of places we have to fill
            # i denotes char index, we can use
            if n==0: return 1
            if i==5: return 0
            return dp(n, i+1) + dp(n-1, i)
        
        return dp(n, 0)
            
            