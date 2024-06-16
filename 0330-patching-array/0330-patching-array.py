class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches, max_num = 0, 0
        i = 0
        
        while max_num < n:
            if i<len(nums) and max_num+1 >= nums[i]:
                max_num += nums[i]; i+=1
            else:
                patches += 1
                max_num += (max_num + 1)
                
        return patches