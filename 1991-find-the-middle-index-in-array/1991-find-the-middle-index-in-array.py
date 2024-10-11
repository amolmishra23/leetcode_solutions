class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        lsum, rsum = 0, sum(nums)
        
        for i,x in enumerate(nums):
            if lsum + x == rsum: return i
            
            lsum += x
            rsum -= x
            
        return -1