class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n, anchor, res = len(nums), 0, float('-inf')
        
        for i in range(n):
            if i>0 and nums[i-1]>=nums[i]: anchor = i
            res = max(res, i-anchor+1)
            
        return res