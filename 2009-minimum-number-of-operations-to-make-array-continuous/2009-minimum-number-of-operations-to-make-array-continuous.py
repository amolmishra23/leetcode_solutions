class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)
        nums = sorted(set(nums))
        r = 0
        res = float("inf")
        
        for l in range(len(nums)):
            # expecting numbers to be in range nums[l]+length
            while r<len(nums) and nums[r]<nums[l]+length:
                r+=1
            res = min(res, length-(r-l))
            
        return res
    