class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums = nums+[nums[0]]
        return max(abs(a-b) for a, b in zip(nums[:-1], nums[1:]))