class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 0 cant be duplicate.
        # we have 1 as non-duplicate index. Anything which is found not duplicate, comparing to nd-1 index. 
        # We can swap 
        # return nd_index as number of elements in array.
        non_duplicate_index = 1
        i = 1
        while i<len(nums):
            if nums[non_duplicate_index-1]!=nums[i]:
                nums[non_duplicate_index], nums[i] = nums[i], nums[non_duplicate_index]
                non_duplicate_index += 1
            i+=1
        
        return non_duplicate_index