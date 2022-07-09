class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # i is index of the house
        # t is remaining number of groups
        # p is previous home color
        @lru_cache(None)
        def dp(i, t, p):
            if i==len(houses) or t<0:
                return 0 if i==len(houses) and t==0 else float('inf')
            
            # house is not painted
            if houses[i]==0:
                # lets paint the house with all possible new colors
                return min(cost[i][nc-1]+dp(i+1, t-(p!=nc), nc) for nc in range(1, n+1))
            else:
                return dp(i+1, t-(houses[i]!=p), houses[i])
            
        return dp(0, target, -1) if dp(0, target, -1)!=float("inf") else -1
                