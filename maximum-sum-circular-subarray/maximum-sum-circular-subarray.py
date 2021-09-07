class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        Question is, assuming array is circular, which subarray could give us max sum
        n**2 solution can be done, starting at ith index to (i-1)th index
        other easy way is, find the max possible sum, and min possible subarray sum (as per kadane algo)
        In the end the result is either just max_sum_possible(straight sum) or (total_sum-min_sum) via the kadane algorithm 
        """
        
        min_, max_, sum_ = min(nums), max(nums), sum(nums)
        
        if min_>=0: return sum_
        if max_<=0: return max_
        
        max_sum, min_sum = nums[:], nums[:]
        
        for i in range(1, len(max_sum)):
            max_sum[i] += max(0, max_sum[i-1])
            min_sum[i] += min(0, min_sum[i-1])
            
        max_sum_res, min_sum_res = max(max_sum), min(min_sum)
        
        return max(max_sum_res, sum_-min_sum_res)