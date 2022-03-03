from collections import deque
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1: return 0
        
        left, prod = 0, 1
        res = 0
        
        for right in range(len(nums)):
            prod *= nums[right]
            
            while left<=right and prod>=k:
                prod/=nums[left]; left+=1
            
            res += right-left+1
                
        return res