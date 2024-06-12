class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, end = 0, len(nums)-1
        curr = 0
        
        while curr<=end:
            if nums[curr]==2:
                nums[curr], nums[end] = nums[end], nums[curr]
                end-=1
            elif nums[curr]==0:
                nums[start], nums[curr] = nums[curr], nums[start]
                start+=1; curr+=1
            elif nums[curr]==1: curr+=1
                
        return nums
        