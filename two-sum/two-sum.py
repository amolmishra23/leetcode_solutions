class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache_ = {}
        
        for i, num in enumerate(nums):
            temp = target-num
            if temp in cache_:
                return [cache_[temp], i]
            cache_[num] = i
            
        return [-1, -1]