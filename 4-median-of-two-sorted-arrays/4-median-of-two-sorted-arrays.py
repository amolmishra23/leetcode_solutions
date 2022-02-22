import heapq

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        max_heap, min_heap = [], []
        
        for num in nums1+nums2:
            if not max_heap or -max_heap[0]>=num:
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)
                
            if len(max_heap)>len(min_heap)+1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif len(min_heap)>len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

        if len(min_heap)==len(max_heap):
            return (-max_heap[0]+min_heap[0])/2
        return -max_heap[0]
        