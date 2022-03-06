class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """
        [[1,4],[3,6],[2,8]]
        
        First we sort it to make as [[1,4], [2,8], [3,6]]
        0 index is already sorted. If end time of ith element is less than prev, for sure interval is covered. So we can skip it.
        If we get [3,10], [3,6]. to cover such cases, we can sort intervals by descending order, and process accordingly. 
        """
        
        intervals.sort(key = lambda x: (x[0], -x[1]))
        
        res, ending = 0, 0
        
        # intervals are sorted first by start time
        # if 2 intervals with same start time, we sort by ending time in descending order
        # if curr interval ending is bigger than prev ending, its new interval
        # otherwise we are good to skip it. 
        for _, end in intervals:
            if end > ending:
                res += 1
                ending = end
                
        return res