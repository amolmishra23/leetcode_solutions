class Solution:
    def minimumTotal(self, arr: List[List[int]]) -> int:
        if not arr: return 0
        
        m, n = len(arr), len(arr[0])
        # we basically come from bottom to up
        # at every level, just check whichever path is cheaper to go. 
        # its cheaper to go from 6 to 1, rather than 6 to 4. 
        # finally we have the answer, which route to traverse from the top. 
        dp = list(arr[-1])
        
        for i in range(m-2, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + arr[i][j]
                
        return dp[0]