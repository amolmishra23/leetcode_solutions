class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        
        b1, s1, b2, s2 = float('-inf'), 0, float('-inf'), 0
        
        for price in prices:
            b1 = max(b1, -price)
            s1 = max(s1, b1+price)
            b2 = max(b2, s1-price)
            s2 = max(s2, b2+price)
            
        return s2