class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = {}
        
        def dfs(i, buying, k):
            if i>=len(prices) or k==0: return 0
            
            if (i, buying, k) in dp: return dp[(i, buying, k)]
            
            if buying:
                buy = -prices[i] + dfs(i+1, not buying, k)
                cooldown = dfs(i+1, buying, k)
                dp[(i, buying, k)] = max(buy, cooldown)
            else:
                sell = prices[i] + dfs(i+1, not buying, k-1)
                cooldown = dfs(i+1, buying, k)
                dp[(i, buying, k)] = max(sell, cooldown)
                
            return dp[(i, buying, k)]
        
        return dfs(0, True, k)