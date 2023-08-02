class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def solve(idx):
            nonlocal res, nums
            if idx==len(nums):
                res.append(list(nums))
                return 
            
            for i in range(idx, len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                solve(idx+1)
                nums[i], nums[idx] = nums[idx], nums[i]
                
        solve(0); return res