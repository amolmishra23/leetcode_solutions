class Solution:
    def isValidTraingle(self, nums):
        return all(nums[i]+nums[j]>nums[k] for i,j,k in [(0,1,2), (1,2,0), (0,2,1)])

    def triangleType(self, nums: List[int]) -> str:
        if not self.isValidTraingle(nums): return "none"

        match len(set(nums)):
            case 1: return "equilateral"
            case 2: return "isosceles"
            case _: return "scalene"
