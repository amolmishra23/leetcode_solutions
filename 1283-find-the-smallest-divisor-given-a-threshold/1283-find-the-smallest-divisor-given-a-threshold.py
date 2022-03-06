class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 0, 10**8
        
        def is_good(divisor):
            return sum(((i-1)//divisor)+1 for i in nums) <= threshold
        
        left, right = 1, max(nums)
        
        while left<=right:
            mid = left + (right-left)//2
            if is_good(mid):
                right = mid-1
            else:
                left = mid+1
                
        return left