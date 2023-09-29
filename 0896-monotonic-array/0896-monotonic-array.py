class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return len({nums[i]>nums[i+1] for i in range(len(nums)-1) if nums[i]!=nums[i+1]})<=1