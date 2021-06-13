class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # question is given wrong, aim is not to reach last block. but next to last block. 
        dp = [float('inf')]*len(cost)
        
        # first one obvious hai
        dp[0] = cost[0]
        # to reach dp[2], either dp[0]+dp[1] or directly dp[1]. Hence this is also obvious. 
        dp[1] = cost[1]
        
        for i in range(2, len(cost)):
            # for everything else, we basically add current cost and see which is cheaper to come from
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        #last one can be reached either from last or 2nd last
        return min(dp[-1], dp[-2])