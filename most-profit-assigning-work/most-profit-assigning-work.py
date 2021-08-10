import bisect

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # this sorts by difficult
        jobs = sorted(zip(difficulty, profit))
        res = i = best = 0
        
        for ability in sorted(worker):
            # iterate all the difficulties less than ability
            # find the best possible profits
            while i<len(jobs) and ability >= jobs[i][0]:
                best = max(jobs[i][1], best)
                i += 1
            
            # add the best possible profit for the particular worker
            res += best
            
        return res
        
            