class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda x: -x, nums))
        heapq.heapify(nums)        
        for _ in range(k-1): heapq.heappop(nums)
        return -heapq.heappop(nums)
            