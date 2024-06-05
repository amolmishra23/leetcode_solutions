class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        mn, mx = res, res
        
        for i in range(1, len(nums)):
            if nums[i]<0: mx, mn = mn, mx
            mx = max(nums[i], mx*nums[i])
            mn = min(nums[i], mn*nums[i])
            if mx>res: res=mx
                
        return res