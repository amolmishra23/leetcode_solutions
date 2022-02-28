class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n, anchor, res = len(nums), 0, float('-inf')
        
        for i in range(n):
            # because the prev element is bigger than curr element
            # we need to reset the anchor. 
            if i>0 and nums[i-1]>=nums[i]: anchor = i
            # we just find how many elements between curr index and the anchor. 
            res = max(res, i-anchor+1)
            
        return res