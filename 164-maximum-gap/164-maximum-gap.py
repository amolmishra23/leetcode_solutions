class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2: return 0
        nums.sort()
        return max(abs(n2-n1) for n1, n2 in zip(nums[1:], nums[:-1]))