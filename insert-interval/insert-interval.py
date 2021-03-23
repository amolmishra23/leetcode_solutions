class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        i, n = 0, len(intervals)
        res = []

        # Skipping all the intervals which end before the new interval
        while i<n and intervals[i][1]<new_interval[0]: 
            res.append(intervals[i])
            i+=1

        while i<n and intervals[i][0]<=new_interval[1]:
            new_interval[0] = min(intervals[i][0], new_interval[0])
            new_interval[1] = max(intervals[i][1], new_interval[1])
            i+=1

        res.append(new_interval)

        while i<n:
            res.append(intervals[i])
            i+=1

        return res