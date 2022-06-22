import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = None
        while k:
            res = heapq.heappop(nums)
            k-=1
        return -res
        