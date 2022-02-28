import statistics

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """Sliding window problem"""
        n = len(nums)
        if n==0: return 0
        if k>n: return sum(nums)/len(nums)
        
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        
        for i in range(k, n):
            curr_sum += nums[i]-nums[i-k]
            max_sum = max(curr_sum, max_sum)
        
        return max_sum/k