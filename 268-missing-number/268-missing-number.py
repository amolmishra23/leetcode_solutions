class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        xor1, xor2 = 0, nums[0]
        for i in range(1, len(nums)+1):
            xor1 ^= i
        for i in range(1, len(nums)):
            xor2 ^= nums[i]
        return xor1 ^ xor2