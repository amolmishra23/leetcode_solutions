class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9+7
        @lru_cache(None)
        def solve(len_):
            if len_==0: return 1
            if len_<0: return 0
            res = solve(len_-zero) + solve(len_-one)
            return res%MOD
        
        res = 0
        for len_ in range(low, high+1):
            res = (res + solve(len_))%MOD
        return res