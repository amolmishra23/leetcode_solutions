class Solution:
    def maxSum(self, nums: List[int]) -> int:
        new = [x for x in nums if x>0]
        if not new: return max(nums)
        return sum(list(set(new)))