class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        Assuming if we have 0,0,0 a subarray, we can get the following sub-arrays from it
        a,b,c
        =====
        a
        a,b
        a,b,c
        b
        b,c
        c
        
        Basically for length of 3, we get 6 subarrays. Its basically 3+2+1. In math way it is n*(n+1)//2
        Just keep finding the continuous 0 arrays and keep finding number of possible subarrays and add to result. 
        """
        nums.append(-1)
        res, count = 0, 0
        
        for num in nums:
            if num==0: count+=1
            else:
                res+=(count*(count+1))//2
                count=0
                
        return res
        