class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        if not prices: return 0
        
        b1, s1, b2, s2 = float('-inf'), 0, float('-inf'), 0
        
        for price in prices:
            b1 = max(b1, -price)
            s1 = max(s1, b1+price)
            b2 = max(b2, s1-price)
            s2 = max(s2, b2+price)
            
        return s2
        """
        
        @functools.lru_cache(None)
        def solve(idx, can_buy, k):
          if idx==len(prices) or k==2: return 0
          
          if can_buy:
            return max(
              solve(idx+1, False, k) - prices[idx],
              solve(idx+1, True, k)
            )
          else:
            return max(
              solve(idx+1, True, k+1)+prices[idx],
              solve(idx+1, False, k)
            )
          
        return solve(0, True, 0)