class Solution:
    def profitableSchemes(self, n: int, min_profit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9+7
        
        @lru_cache(None)
        def dp(i, curr_profit, curr_people):
            if i>=len(group): return curr_profit>=min_profit
            
            res = 0
            if curr_people+group[i] <= n:
                res = (res + dp(i+1, min(curr_profit+profit[i], min_profit), curr_people+group[i]))%MOD
            res = (res + dp(i+1, curr_profit, curr_people))%MOD
            
            return res
        
        return dp(0, 0, 0)