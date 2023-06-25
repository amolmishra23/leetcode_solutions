class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 1000000007
        @lru_cache(None)
        def solve(curr_city, fuel_left):
            if fuel_left < 0: return 0
            res = 1 if curr_city == finish else 0
            for idx in range(len(locations)):
                if idx==curr_city: continue
                res = (res + solve(idx, fuel_left - abs(locations[idx] - locations[curr_city]))) % MOD
                
            return res
        
        return solve(start, fuel)
            