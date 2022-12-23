class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        
        def dfs(i, buying):
            if i>=len(prices): return 0
            
            if (i, buying) in dp: return dp[(i, buying)]
            
            if buying:
                buy = -prices[i] + dfs(i+1, False)
                dont_buy = dfs(i+1, True)
                dp[(i, buying)] = max(buy, dont_buy)
            else:
                sell = prices[i] + dfs(i+2, True)
                dont_sell = dfs(i+1, False)
                dp[(i, buying)] = max(sell, dont_sell)
                
            return dp[(i, buying)]
        
        return dfs(0, True)