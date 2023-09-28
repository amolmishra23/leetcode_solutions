class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r, n = 0, 0, len(nums)
        
        while r<n:
            if nums[r]%2:
                r+=1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r+=1
                
        return nums
        