class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0
        
        for i in range(n):
            if total_sum-left_sum-nums[i]==left_sum:
                return i
            left_sum+=nums[i]
            
        return -1