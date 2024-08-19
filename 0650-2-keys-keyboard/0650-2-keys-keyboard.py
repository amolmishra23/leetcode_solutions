class Solution:
    def minSteps(self, n: int) -> int:
        dp = [1000]*(n+1)
        dp[1] = 0
        
        for i in range(2, n+1):
            for j in range(1, 1+(i//2)):
                if i%j == 0:
                    dp[i] = min(dp[i], dp[j] + i//j)
                    
        return dp[n]