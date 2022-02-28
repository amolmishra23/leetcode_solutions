class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        The idea is that sort it based on endtime. 
        (1,20) (2,5) (7,9)
        If we sort by end time only 1 we should remove.
        Else we will have to remove 2 of it. 
        """
        end, cnt = float('-inf'), 0
        for s, e in sorted(intervals, key=lambda x: x[1]):
            if s >= end: 
                end = e
            else: 
                cnt += 1
        return cnt
