class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_ = max(nums)
        res, count = 0, 0
        
        for n in nums:
            if n==max_: count+=1
            else: count=0
            res = max(res, count)
            
        return res