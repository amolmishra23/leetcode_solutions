class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        Same as the problem: https://leetcode.com/problems/maximum-performance-of-a-team/
        """
        
        res, curr_sum = 0, 0
        heap = []
        
        for a, b in sorted(list(zip(nums1, nums2)), key = lambda x: -x[1]):
            heapq.heappush(heap, a)
            curr_sum += a
            if len(heap)>k:
                curr_sum -= heapq.heappop(heap)
            if len(heap) == k:
                res = max(res, curr_sum*b)
        
        return res