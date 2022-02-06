class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Simple solution using 2 pointer approach. 
        # Exchange number at non_dup, if its not equal to number at non_dup-2 index.
        # if we find duplicate we just keep proceeding further, doing nothing. 
        non_dup, i = 2, 2
        
        while i<len(nums):
            if nums[non_dup-2]!=nums[i]:
                nums[non_dup], nums[i] = nums[i], nums[non_dup]
                non_dup += 1
            i+=1
            
        return non_dup