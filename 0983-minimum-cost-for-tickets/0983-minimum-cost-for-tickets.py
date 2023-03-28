class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @lru_cache(None)
        def solve(idx):
            if idx>=len(days): return 0
            
            cost_1 = costs[0]+solve(idx+1)
            
            tmp=idx+1
            while tmp<len(days) and days[tmp]<=days[idx]+6: tmp+=1
            cost_7 = costs[1]+solve(tmp)
            
            tmp=idx+1
            while tmp<len(days) and days[tmp]<=days[idx]+29: tmp+=1
            cost_30 = costs[2]+solve(tmp)
            
            return min(cost_1, cost_7, cost_30)
        
        return solve(0)