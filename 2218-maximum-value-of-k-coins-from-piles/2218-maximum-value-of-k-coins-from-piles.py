class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @lru_cache(None)
        def solve(i, k):
            # base condition to return once we dont need any coins.
            # or are done with the piles. 
            if k==0 or i==len(piles): return 0
            
            # Dont choose any coin from the ith pile
            res, curr_sum = solve(i+1, k), 0
            
            # We can choose between 1..k coins from the current pile[i]
            # Trying out all choices, and then going on solving dp problem
            for j in range(min(k, len(piles[i]))):
                # picked up the coin at jth index in pile[i]
                curr_sum += piles[i][j]
                # assuming we picked upto index j, means we picked j+1 coins. 
                # so in our dp state, we will pass on (i+1, k-(j+1))
                # also add the curr_sum to our result
                res = max(res, curr_sum + solve(i+1, k-(j+1)))
                
            # returning the max value possible
            return res
        
        # we start our problem at index 0, and we need to fill k coins. 
        return solve(0, k)
                