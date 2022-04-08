class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(i, even):
            if i==len(nums): return 0
            
            incl = (nums[i] if even else -1*nums[i]) + dp(i+1, even^1)
            excl = dp(i+1, even)
            
            return max(incl, excl)
        
        return dp(0, 1)