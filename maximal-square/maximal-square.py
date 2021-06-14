class Solution:
    def maximalSquare(self, arr: List[List[str]]) -> int:
        """
        How can we close a square? 
        Basically all the 3 vertices also should have 1. 
        If all are itself a square, then even easier to close square. 
        """
        if len(arr)==0: return 0
        m, n = len(arr), len(arr[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        res_=0
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if arr[i-1][j-1]=="1":
                    dp[i][j] = 1+min(
                        dp[i-1][j-1] if i>=1 and j>=1 else 0,
                        dp[i-1][j] if i>=1 else 0,
                        dp[i][j-1] if j>=1 else 0
                    )
                    res_ = max(res_, dp[i][j])
        
        return res_*res_
        