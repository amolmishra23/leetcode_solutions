class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n =len(nums)
        heap, max_ = [], float("-inf")
        
        for i in range(n):
            heapq.heappush(heap, (nums[i][0], 0, nums[i]))
            max_ = max(max_, nums[i][0])
            
        start, end = heap[0][0], max_
        
        while len(heap) == len(nums):
            # process smallest elem in heap
            elem, idx, arr = heapq.heappop(heap)
            
            # updating min and max in this iteration
            if (max_ - elem) < (end-start):
                start = elem
                end = max_
                
            # adding new element to heap from which we had popped
            if idx+1 < len(arr):
                heapq.heappush(heap, (arr[idx+1], idx+1, arr))
                max_ = max(max_, arr[idx+1])
                
        # returning smallest range of elements from all heaps
        return [start, end]