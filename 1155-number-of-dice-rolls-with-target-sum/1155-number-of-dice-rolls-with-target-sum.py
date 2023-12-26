class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = (10**9)+7
        
        @lru_cache(None)
        def solve(dice, curr_sum):
            if dice>n: return 0
            if dice==n and curr_sum==target: return 1
            return sum(solve(dice+1, curr_sum+val) for val in range(1, k+1)) % MOD
        
        return solve(0, 0)