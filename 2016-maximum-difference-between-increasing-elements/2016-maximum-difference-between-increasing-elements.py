class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        min_ = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i]<=min_:
                min_ = nums[i]
            else:
                res = max(res, nums[i]-min_)
                
        return res