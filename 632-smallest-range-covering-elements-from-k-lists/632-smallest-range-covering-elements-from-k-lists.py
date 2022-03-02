import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        heap = []
        max_ = float('-inf')
        
        for i in range(n):
            heapq.heappush(heap, (nums[i][0], 0, nums[i]))
            max_=max(max_, nums[i][0])
        
        start, end = heap[0][0], max_
        
        while len(heap)==len(nums):
            elem, idx, arr = heapq.heappop(heap)
            curr_range = max_-elem
            
            if curr_range<(end-start):
                end = max_
                start = elem
                
            if idx+1<len(arr):
                heapq.heappush(heap, (arr[idx+1], idx+1, arr))
                max_ = max(max_, arr[idx+1])
        
        return [start, end]