class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        [6,2,1,5,4,3,0]
        """
        n, k = len(nums), None
        for i in range(n-2, -1, -1):
            if nums[i]<nums[i+1]:
                k = i
                break
        else:
            nums.reverse()
            return 
        
        j = None
        for j in range(n-1, -1, -1):
            if nums[j]>nums[i]: break
        
        nums[k], nums[j] = nums[j], nums[k]
        nums[k+1:] = nums[:k:-1]
        return nums