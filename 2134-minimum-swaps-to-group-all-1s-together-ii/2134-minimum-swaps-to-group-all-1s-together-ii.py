class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total_ones, curr_ones = nums.count(1), 0
        l = 0
        
        max_ones = 0
        for r in range(2*n):
            if nums[r%n]:
                curr_ones += 1
            if r-l+1 > total_ones:
                curr_ones -= nums[l%n]
                l += 1
            max_ones = max(max_ones, curr_ones)
            
        return total_ones - max_ones
        