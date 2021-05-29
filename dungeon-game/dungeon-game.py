class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        def solve(i, j, arr, res):
            # if we are stepping out of bounds, like from (2,2) to (2,3) or (3,2) we should short circuit there in order to get solution
            if i>len(arr)-1 or j>len(arr[0])-1: return float('inf')
            if (i, j) in res: return res[(i,j)]
            
            # in order to reach the destination, which of the path is least cost. We choose that. 
            # as we can only move to the right or bottom hence the indexes are accordingly.
            next_ = min(solve(i+1, j, arr, res), solve(i, j+1, arr, res))
            
            # if we are in last cell, reaching with 1 health in end is enough. Hence we substritute max(inf, inf) as 1. 
            if next_==float('inf'): next_=1
                
            # if health at (1,2) is 1. And at (2,2) is -5. Means we need atleast 6 when we step on (2,2)
            # to calculate it, we either find next-curr. If it goes to negative we dont need negative health but +1 would suffice. 
            val = max(next_-arr[i][j], 1)
            res[(i,j)] = val
            return val
        
        if not dungeon or len(dungeon)==0 or len(dungeon[0])==0: return 0
        res = {}
        return solve(0, 0, dungeon, res)
        
            