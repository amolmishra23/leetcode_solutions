class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # we make a zipped list like [s1, e1, p1] etc. 
        # also sort it based on end time.
        # if 2 events start at same time, one that ends later, will come later. 
        jobs = sorted(zip(startTime, endTime, profit), key = lambda v: v[1])
        
        # at ending of 0, we have made 0 profit by far.
        dp = [[0, 0]]
        
        for s, e, p in jobs:
            # we find the nearest ending below our start. 
            # and see, if that_profit+curr_profit is worth going for. (than the last profit we recorded)
            i = bisect.bisect(dp, [s+1])-1
            if dp[i][1]+p>dp[-1][1]:
                # if its better, we save the same
                dp.append([e, dp[i][1]+p])
        
        # return the last profit. 
        return dp[-1][1]