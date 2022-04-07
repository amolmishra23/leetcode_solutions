class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        
        @lru_cache(None)
        def solve(idx, target):
            if target==0: return 1
            if target<0: return 0
            if idx>=n: return 0
            return solve(idx, target-coins[idx]) + solve(idx+1, target)
        
        return solve(0, amount)