class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = 0
        for n in nums:
            maxOr |= n
        cache = [[-1]*(maxOr+1) for _ in range(len(nums))]
            
        def dfs(i, currOr):
            nonlocal maxOr
            
            if i==len(nums):
                return 1 if currOr == maxOr else 0
            
            if cache[i][currOr] != -1:
                return cache[i][currOr]
            
            cache[i][currOr] = dfs(i+1, currOr) + dfs(i+1, currOr | nums[i])
            return cache[i][currOr]
        
        return dfs(0, 0)