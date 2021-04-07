class Solution:
    def minimumTotal(self, arr: List[List[int]]) -> int:
        if len(arr)==0: return 0
        rows = len(arr)
        """
        First we got to cache, min path to reach last row
        From r-1 to r, we will move based on whichever is minimum at c, c+1
        We do this logic via DP
        dp[j] = min(dp[j], dp[j+1]) + arr[i][j]
        """
        dp = list(arr[-1])
        
        for i in range(rows-2, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + arr[i][j]
                
        return dp[0]
        