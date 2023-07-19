class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        currEnd is not guaranteed to be < x.end (eg: [[1, 5], [2, 3], [3, 4]]). 
        After comparing [1, 5] and [2, 3], currEnd must be 3. If it's 5, then 2 intervals will be removed instead of 1.
        """
        if not intervals: return 0
        
        intervals.sort(key = lambda x: x[0])
        min_end = intervals[0][1]
        res = 0
        
        for s, e in intervals[1:]:
            if s<min_end:
                res += 1
                min_end = min(min_end, e)
            else:
                min_end = e
                
        return res
        