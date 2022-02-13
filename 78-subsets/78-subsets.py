class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def solve(nums, curr, res, i):
            if i==len(nums):
                res.append(list(curr))
                return 
            
            solve(nums, curr, res, i+1)
            curr.append(nums[i])
            solve(nums, curr, res, i+1)
            curr.pop()
            
        res = []
        solve(nums, [], res, 0)
        return res