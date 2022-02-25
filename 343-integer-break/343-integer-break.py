class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=2: return 1
        
        dp = [0]*(n+1)
        # Because even for dp[2], best way to split is 1+1, and 1*1=1
        dp[1], dp[2] = 1, 1
        
        for i in range(3, n+1):
            for j in range(1, i):
                """
                The reason for this being, in case of 5 we can either write it as 2+3 or as 2+2+1
                To do as 2+3 => j*(i-j)
                To do as 2+2+1 => j*dp[i-j], which inturn finds the best answer for 3. 
                Hence its done that way!
                """
                dp[i] = max(dp[i], max(j*dp[i-j], j*(i-j)))
                
        return dp[n]