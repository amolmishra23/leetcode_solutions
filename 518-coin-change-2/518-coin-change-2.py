class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def coin_change(idx, target):
            if target==0: return 1
            
            if target<0: return 0
            
            if idx>=len(coins): return 0
            
            return coin_change(idx, target-coins[idx])+coin_change(idx+1, target)
        
        return coin_change(0, amount)