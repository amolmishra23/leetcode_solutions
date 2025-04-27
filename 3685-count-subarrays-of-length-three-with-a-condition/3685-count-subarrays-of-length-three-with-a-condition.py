class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        return sum(a+c+a+c==b for a,b,c in zip(nums[:], nums[1:], nums[2:]))
            