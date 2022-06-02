class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(None)
        def dp(left, right):
            if left >= right:
                return 0
            
            res = math.inf
            
            for node in range(left, right+1):
                left_cost = dp(left, node-1)
                right_cost = dp(node+1, right)
                res = min(res, max(left_cost, right_cost)+node)
                
            return res
        
        return dp(1, n)