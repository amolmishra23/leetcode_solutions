class Solution:
    def numSquares(self, n: int) -> int:
        """
        In order to solve for 12, lets say int(sqrt(12))=3
        So we try 3*3=9. 12-9=3
        So for 3 again we solve. We need 3 perfect squares(1)
        In total we need 9+1+1+1 (4 in total)
        
        If we go by using 2. We use 4 and again for 8 it comes most optimal as 4+4
        Hence we need 4+4+4=12 (3 in total)
        
        
        """
        if n<=0: return 0
        
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        
        for i in range(1, n+1):
            for j in range(1,i+1):
                if not j*j<=i: break
                # because if we use j*j, we are using 1 number.
                # for the residual i-(j*j), we check how many minimal perfect squares do we need. 
                dp[i] = min(dp[i], dp[i-(j*j)]+1)
        
        return dp[n]
        