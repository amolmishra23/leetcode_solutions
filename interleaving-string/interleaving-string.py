class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        def solve(i, j, k):
            if k==len(s3): return True
            if i==len(s1) and j==len(s2): return False
            
            res = []
            if i<len(s1) and s1[i]==s3[k]:
                res.append(solve(i+1, j, k+1))
            
            if j<len(s2) and s2[j]==s3[k]:
                res.append(solve(i, j+1, k+1))
            
            return any(res)
            
        return solve(0,0,0)
        """
        
        if len(s3) != len(s1)+len(s2): return False
        
        dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
        
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i==0 and j==0: dp[i][j]=True
                elif i==0: dp[i][j] = dp[i][j-1] and s2[j-1] == s3[j-1]
                elif j==0: dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i-1]
                else: dp[i][j] = (dp[i][j-1] and s2[j-1]==s3[i+j-1]) or (dp[i-1][j] and s1[i-1]==s3[i+j-1])
        
        return dp[len(s1)][len(s2)]