class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, curr_sum = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            # either the curr streak can be adding curr number, or just 1 number alone(if its negative numbers)
            # then we keep updating the max_sum
            curr_sum = max(curr_sum+nums[i], nums[i])
            max_sum = max(max_sum, curr_sum)
            
        return max_sum