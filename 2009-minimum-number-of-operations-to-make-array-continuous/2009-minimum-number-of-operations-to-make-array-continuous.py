class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))  

        ans = n
        for i, start in enumerate(nums):
            end = start + n - 1 
            idx = bisect_right(nums, end)
            uniqueLen = idx - i
            ans = min(ans, n - uniqueLen)
        return ans
    
    def minOperations1(self, nums: List[int]) -> int:
        length = len(nums)
        nums = sorted(set(nums))
        r = 0
        res = float("inf")
        
        for l in range(len(nums)):
            # expecting numbers to be in range nums[l]+length-1
            while r<len(nums) and nums[r]<=nums[l]+length-1:
                r+=1
            res = min(res, length-(r-l))
            
        return res
    