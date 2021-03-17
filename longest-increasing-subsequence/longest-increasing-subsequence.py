class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        temp = [1]*len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j]<nums[i]: temp[i] = max(temp[i], temp[j]+1)
        
        return max(temp)