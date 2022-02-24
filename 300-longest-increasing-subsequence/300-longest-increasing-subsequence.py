class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1]*len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j]<nums[i]: lis[i] = max(lis[i], lis[j]+1)
        
        return max(lis)