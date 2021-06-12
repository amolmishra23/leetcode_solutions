class Solution:
    def coinChange(self, arr: List[int], n: int) -> int:
        m = len(arr)
        
        dp = [[None]*(n+1) for _ in range(m+1)]
        """
        dp table rows are basically using until xth coins
        dp table cols are basically for that particular amount y
        Lets think of a few questions. 
        Min coins to make 0,1,2,...n amount. when 0 coins avlb. float('inf')
        Min coins to make amount 0 when we have supply of 1,2..n coins. 0
        Min coins to make amount 0, when we have 0 coins. 0
        """
            
        for i in range(m+1):
            for j in range(n+1):
                if i==0: dp[i][j] = float('inf')
                elif j==0: dp[i][j] = 0
                elif (arr[i-1] <= j):
                    dp[i][j] = min(dp[i-1][j], 1+dp[i][j-arr[i-1]])
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[m][n] if dp[m][n]!=float('inf') else -1