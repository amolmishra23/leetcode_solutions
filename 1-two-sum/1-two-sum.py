class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        
        for i, num in enumerate(nums):
            if target-num in prev:
                return (prev[target-num], i)
            prev[num] = i
            
        return (-1, -1)