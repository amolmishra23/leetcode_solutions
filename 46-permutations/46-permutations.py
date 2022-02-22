class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def solve(idx):
            if idx==len(nums):
                self.res.append(list(nums))
                return 
            
            for i in range(idx, len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                solve(idx+1)
                nums[i], nums[idx] = nums[idx], nums[i]
                
        self.res = []
        solve(0)
        return self.res