class Solution:
    def twoCitySchedCostDp(self, costs: List[List[int]]) -> int:
        n = len(costs)
        
        @lru_cache(None)
        def solve(idx, n1, n2):
            if idx>=n: 
                return 0
            
            res = float('inf')
            if n1:
                res = min(res, costs[idx][0] + solve(idx+1, n1-1, n2))
            if n2:
                res = min(res, costs[idx][1] + solve(idx+1, n1, n2-1))
                
            return res

        return solve(0, n//2, n//2)
        
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # sorting it in profit of going to city 1. 
        # take 1st n//2 people to city1 and others to city2. 
        costs.sort(key=lambda cost: cost[0] - cost[1])
        costs_for_A = sum([cost[0] for cost in costs[:len(costs) // 2]])
        costs_for_B = sum([cost[1] for cost in costs[len(costs) // 2:]])
        return costs_for_A + costs_for_B
