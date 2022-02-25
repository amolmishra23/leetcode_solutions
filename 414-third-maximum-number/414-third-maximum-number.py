import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        n = len(nums)
        k = 3
        if n<k: return max(nums)
        else:
            heapq.heapify(nums)
            return heapq.nlargest(k, nums)[-1]
            # for _ in range(k):
            #     res = heapq._heappop_max(nums)
            # return res