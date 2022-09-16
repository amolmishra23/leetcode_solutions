class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)
        
        dp = [[0]*(m+1) for _ in range(m+1)]
        
        for op in range(m-1, -1, -1):
            for left in range(op, -1, -1):
                l = (multipliers[op] * nums[left]) + dp[op+1][left+1]
                r = (multipliers[op] * nums[(n-1)-(op-left)]) + dp[op+1][left]
                dp[op][left] = max(l, r)
        
        return dp[0][0]