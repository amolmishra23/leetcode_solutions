class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
# its tricky because the array is unsorted., 
# make sure elements less than x doesnt exist in the list
# then we go as deep as possible. dfs. sequentially. 
# 1->2->3->4.
# find the max such element
        if not nums: return 0
        result = 0
        
        nums_set = set(nums)
        
        for num in nums_set:
            count = 1
            if not (num-1 in nums_set):
                while (num+1 in nums_set):
                    count += 1
                    num += 1
                result = max(result, count)
        
        return result