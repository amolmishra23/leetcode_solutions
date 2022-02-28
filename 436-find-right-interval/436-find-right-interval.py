import heapq

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start, end = [], []
        res = [None]*len(intervals)
        
        for i in range(len(intervals)):
            # store the start and end times of the intervals in a max heap
            heapq.heappush(start, (-intervals[i][0], i))
            heapq.heappush(end, (-intervals[i][1], i))
            
        for _ in range(len(intervals)):
            # pop the end time from the heap. 
            top_end, end_index = heapq.heappop(end)
            res[end_index] = -1
            
            # checking for the current end time, which is the next bigger start time
            if -start[0][0] >= -top_end:
                # pop all the startups, until last one remains. 
                while start and -start[0][0] >= -top_end:
                    top_start, start_index = heapq.heappop(start)
                
                # this is the answer. 
                res[end_index] = start_index
                
                # push it back to the queue, as it may be answer to others. 
                heapq.heappush(start, (top_start, start_index))
        
        return res
