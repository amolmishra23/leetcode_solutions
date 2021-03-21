class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def solve(str1, str2):
            m, n = len(str1), len(str2)
            
            dp = [[float('inf')]*(n+1) for _ in range(m+1)]
            dp[0][0] = 0
            
            for i in range(n+1): dp[0][i] = i
            for i in range(m+1): dp[i][0] = i
            
            for i in range(1, m+1):
                for j in range(1, n+1):
                    if str1[i-1]==str2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
                        
            return dp[m][n]
        
        return solve(word1, word2)