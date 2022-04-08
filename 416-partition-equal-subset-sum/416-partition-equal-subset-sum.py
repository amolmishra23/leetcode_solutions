class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dp(idx, target):
            if target == 0: return True
            
            if idx>=len(nums): return False
            
            return dp(idx+1, target-nums[idx]) or dp(idx+1, target)
        
        s = sum(nums)
        if s%2!=0: return False
        return dp(0, s//2)