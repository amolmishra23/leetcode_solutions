class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        
        # robbing house at ith index gives us 0
        # question is, which other alternate houses to rob, and which particular permutation sequence gives us max profit?
        # we use dp to solve the same
        
        if len(nums)<=2: return max(nums)
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
            
        return dp[-1]