class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stk, res = [], 0
        
        for i, num in enumerate(nums):
            if not stk or nums[stk[-1]]>nums[i]:
                stk.append(i)
                
        for j in range(len(nums)-1, -1, -1):
            while stk and nums[stk[-1]]<=nums[j]:
                i = stk.pop()
                res = max(res, j-i)
                
        return res