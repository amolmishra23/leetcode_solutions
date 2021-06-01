class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        
        if len(nums)<=2: return max(nums)
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        
        for x in range(2, len(nums)):
            dp[x] = max(dp[x-1], nums[x]+dp[x-2])
            
        return dp[-1]
        