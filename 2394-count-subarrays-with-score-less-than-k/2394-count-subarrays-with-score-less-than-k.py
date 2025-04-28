class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res, currSum, l = 0, 0, 0
        
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum * (r-l+1) >= k:
                currSum -= nums[l]
                l += 1
            res += (r-l+1)
        
        return res