class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
#         @lru_cache(None)
#         def solve(idx, prev):
#             if idx == len(colors): return 0
#             notIncl = neededTime[idx] + solve(idx+1, prev)
#             if prev and colors[idx]==prev:
#                 return notIncl
#             incl = solve(idx+1, colors[idx])
#             return min(incl, notIncl)
        
#         return solve(0, None)
    
        res = 0
        
        for i in range(1, len(colors)):
            if colors[i]==colors[i-1]:
                res += min(neededTime[i], neededTime[i-1])
                neededTime[i] = max(neededTime[i], neededTime[i-1])
                
        return res