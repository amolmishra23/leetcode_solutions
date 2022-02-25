class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        Logic being, subarray is only related to prev element in the current streak
        in case whatever streaks we found till a point, we keep adding it in the res variable. 
        and return res variable in the end. 
        """
        curr, res = 0, 0
        
        for i in range(2, len(nums)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                curr += 1
                res += curr
            else:
                curr = 0
                
        return res