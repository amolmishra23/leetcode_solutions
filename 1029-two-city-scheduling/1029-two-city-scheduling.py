class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
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
                