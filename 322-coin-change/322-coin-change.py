class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        
        @lru_cache(None)
        def solve(idx, target):
            if target==0: return 0
            if target<0: return float('inf')
            if idx >= n: return float('inf')
            
            return min(1+solve(idx, target-coins[idx]), solve(idx+1, target))
        
        return -1 if solve(0, amount)==float('inf') else solve(0, amount)