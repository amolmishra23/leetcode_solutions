class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr, res = 0, 0
        
        for num in nums:
            curr = curr+1 if num==1 else 0
            res = max(res, curr)
            
        return res