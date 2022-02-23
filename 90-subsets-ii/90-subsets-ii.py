class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def solve(nums, i, curr, res):
            if i==len(nums):
                res.add(tuple(curr))
                return 
            
            solve(nums, i+1, curr, res)
            curr.append(nums[i])
            solve(nums, i+1, curr, res)
            curr.pop()
        
        res = set()
        nums.sort()
        solve(nums, 0, [], res)
        return list(res)