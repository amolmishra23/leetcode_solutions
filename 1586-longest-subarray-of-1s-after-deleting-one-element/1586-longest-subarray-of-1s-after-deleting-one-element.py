class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i, res, count = 0, 0, 0
        
        for j in range(len(nums)):
            if nums[j]==0:
                count += 1
                
            while count>1:
                if nums[i]==0:
                    count-=1
                i += 1
            
            res = max(res, j-i+1-count)
            
        # because 1 number needs to be deleted mandatorily
        return res if res!=len(nums) else res-1
            