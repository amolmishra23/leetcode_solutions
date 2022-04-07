class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        mx, mn = res, res
        
        for i in range(1, len(nums)):
            if nums[i]<0: mx, mn = mn, mx
            mx = max(nums[i], mx*nums[i])
            mn = min(nums[i], mn*nums[i])
            res = max(res, mx)
        
        return res