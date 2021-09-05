class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [float('inf')]*len(cost)
        
        # to reach ith place, we will obv have to spend cost[i]
        # the question is, do we jump from i-1 or i-2 th places
        # thats based on dp whichever comes minimum
        
        dp[0] = cost[0]+0
        dp[1] = cost[1]+0
        
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
            
        return min(dp[-1], dp[-2])
        
        