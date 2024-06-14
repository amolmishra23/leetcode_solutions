class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        
        for i in range(1, len(nums)):
            if nums[i-1]>=nums[i]:
                res += nums[i-1]-nums[i]+1
                nums[i] = nums[i-1]+1
                
        return res
        
    def minIncrementForUnique1(self, nums: List[int]) -> int:
        count, res = Counter(nums), 0
        
        for i in range(len(nums) + max(nums)):
            if count[i]>1:
                extra = count[i]-1
                count[i+1] += extra
                res += extra
                
        return res