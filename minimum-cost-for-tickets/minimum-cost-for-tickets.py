class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        def solve(days, costs, idx):
            if idx in dp: return dp[idx]
            if idx>=len(days): return 0
            
            # if we buy 1 day pass, we need to have pass from next index onwards. 
            cost_1 = costs[0] + solve(days, costs, idx+1)
            
            # finding until which index are we secured, if we buy a 7 day pass
            # because the days are not continuous, need to find exact index, until which are are good to not buy any pass. 
            i = idx
            while i<len(days) and days[i]<days[idx]+7: i+=1
            cost_7 = costs[1] + solve(days, costs, i)
            
            # finding until which index are we secured, if we buy a 30 day pass
            i = idx
            while i<len(days) and days[i]<days[idx]+30: i+=1
            cost_30 = costs[2] + solve(days, costs, i)
            
            dp[idx] = min(cost_1, cost_7, cost_30)
            return dp[idx]
        
        return solve(days, costs, 0)