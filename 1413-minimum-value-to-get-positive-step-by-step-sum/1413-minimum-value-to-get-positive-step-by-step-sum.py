class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        """
        Minimum most value in the prefix sum array possible. 
        1-that value is result. 
        [-3,2,-3,4,2]
        -3, -1, -4, 0, 2
        Because example at one point, lowest we can go is -4. If we started from +5, our lowest value would go only to 1. 
        Hence proved.
        """
        
        prefix_sum, min_val = 0, float('inf')
        
        for num in nums:
            prefix_sum += num
            min_val = min(min_val, prefix_sum)
            
        return max(1-min_val, 1)