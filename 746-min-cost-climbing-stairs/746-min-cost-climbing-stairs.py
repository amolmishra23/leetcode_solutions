class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(None)
        def solve(idx):
            if idx>=len(cost): return 0
            
            return cost[idx] + min(solve(idx+1), solve(idx+2))
        
        return min(solve(0), solve(1))