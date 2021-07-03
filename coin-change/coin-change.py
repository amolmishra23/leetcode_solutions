class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def coin_change(coins, idx, target):
          if (idx, target) in cache: return cache[idx, target]
          if target==0: return 0;

          if target<0 or idx>=len(coins): return float('inf')

          cache[idx, target] = min(1+coin_change(coins, idx, target-coins[idx]), coin_change(coins, idx+1, target))

          return cache[idx,target]
    
        cache={}
        res = coin_change(coins, 0, amount)
        
        return res if res!=float('inf') else -1