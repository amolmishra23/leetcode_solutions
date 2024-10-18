class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = 0
        for n in nums:
            maxOr |= n
            
        def dfs(i, currOr):
            nonlocal maxOr
            
            if i==len(nums):
                return 1 if currOr == maxOr else 0
            
            return dfs(i+1, currOr) + dfs(i+1, currOr | nums[i])
        
        return dfs(0, 0)