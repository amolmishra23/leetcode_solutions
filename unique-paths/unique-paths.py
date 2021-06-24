class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Basic idea is that we can reach at (i,j) either from (i-1,j) and (i,j-1)
        So we basically add up how many ways we can reach both of them. And that becomes our solution to the problem. 
        """
        dp = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i==0 and j==0: dp[i][j]=1
                if i>0: dp[i][j] += dp[i-1][j]
                if j>0: dp[i][j] += dp[i][j-1]
                    
        return dp[m-1][n-1]