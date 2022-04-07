class Solution:
    def maximalSquare(self, arr: List[List[str]]) -> int:
        if len(arr)==0: return 0
        
        m, n = len(arr), len(arr[0])
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        res = 0
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if arr[i-1][j-1]=="1":
                    dp[i][j] = 1+min(
                        dp[i-1][j-1], dp[i-1][j], dp[i][j-1]
                    )
                    res = max(res, dp[i][j])
                
        return res*res