class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Example of when freq is:
        1: cant solve. return -1
        7: writing as multiples of 3,2 it will be 3*1+2*2. Hence it comes as 7//3+1
        8: writing as multiples of 3,2 it will be 3*2+2*1. It again comes as 8//3+1
        """
        res = 0
        
        for k,v in Counter(nums).items():
            if v==1: return -1
            elif v%3==0:
                res += v//3
            else:
                res += v//3 + 1
            
        return res