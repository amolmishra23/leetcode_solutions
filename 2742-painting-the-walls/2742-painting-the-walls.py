class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        @lru_cache(None)
        def dp(i, rem):
            # We have 0 walls remaining. Success case
            if rem<=0: return 0
            
            # we reached end (skipping all choices). Painting not done.
            # failure sequence
            if i==len(cost): return float("inf")
            
            # lets paint the current wall.
            # lets skip paiting the current wall.
            
            # we have only condensed it to 2 variable dp.
            # no need to track time. Because instead of tracking time,
            # we keep reducing that many walls in the remaining walls.
            # ultimately if we have 0 remaining walls, that anyways is our soln. 
            return min(cost[i] + dp(i+1, rem - 1 - time[i]), dp(i+1, rem))
        
        return dp(0, len(time))
            