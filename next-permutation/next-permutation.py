class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k, l = -1, 0
        n = len(nums)
# need to find the first number before start of the decreasing sequence
# Example [6, 2, 1, 5, 4, 3, 0]
# So 1 is the number found.
# In strictly decreasing sequence, 3 is the first number bigger than 1. So exchange it. 
# [6, 2, 3, 5, 4, 1, 0]
# Now reverse the remaining array. [6, 2, 3, 0, 1, 4, 0], as it is the first permutation, Return the result
        for i in range(n-2, -1, -1):
            if nums[i]<nums[i+1]:
                k = i
                break
        else:
            nums.reverse()
            return
    
        for i in range(n-1, k, -1):
            if nums[i]>nums[k]:
                l = i
                break
        nums[k], nums[l] = nums[l], nums[k]
        nums[k+1:] = nums[:k:-1]
        return nums