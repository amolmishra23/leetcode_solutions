class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Aim in this question being, to find shortest path.
        We need to break it down and see which is shorter. Whether the left one or top one.
        And we can conclude on our answer. 
        """
        m, n = len(grid), len(grid[0])
        
        dp = [[None]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i==0 and j==0: dp[i][j]=grid[i][j]
                else: 
                    dp[i][j] = min(dp[i-1][j] if i>=1 else float('inf'), dp[i][j-1] if j>=1 else float('inf')) + grid[i][j]
        
        return dp[-1][-1]