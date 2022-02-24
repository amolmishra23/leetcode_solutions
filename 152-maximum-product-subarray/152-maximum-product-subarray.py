class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        max_, min_ = res, res
        
        for i in range(1, len(nums)):
            # if curr num is -ve, max can be obtained by multiplying with most min_ number. 
            # hence this swap
            if nums[i]<0: max_, min_ = min_, max_
                
            # checking like kadane algorithm. if max is by continuing the streak or starting from this index
            max_ = max(nums[i], max_*nums[i])
            # because of -ve numbers occurence, we also have to keep finding the -ve most elem as per kadane algo
            min_ = min(nums[i], min_*nums[i])
            
            # keep updating the result
            res = max(res, max_)
            
        return res