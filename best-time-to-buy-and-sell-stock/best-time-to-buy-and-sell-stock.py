class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_, max_profit = float('inf'), 0
        
        for price in prices:
            if price<min_:
                min_ = price
            else:
                max_profit = max(max_profit, price-min_)
                
        return max_profit