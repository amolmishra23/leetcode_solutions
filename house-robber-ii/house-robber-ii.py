class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        
        # if 3 or less than 3 nums, for sure we can rob only 1 house because of circular condition. 
        # return the max value among them
        if len(nums)<=3: return max(nums)
        
        def solve(dp):
            # very similar to house robber 1 ka approach
            dp[1] = max(dp[0], dp[1])
            
            for i in range(2, len(dp)):
                dp[i] = max(dp[i-1], dp[i]+dp[i-2])
            
            return dp[-1]
        
        # because of the circular condition, if we include 1st, cant include last, and vice versa.
        # Hence we find what is the best we can do in both the cases and return the response. 
        return max(solve(nums[:len(nums)-1]), solve(nums[1:]))