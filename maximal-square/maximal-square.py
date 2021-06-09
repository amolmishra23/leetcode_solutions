class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        In order to calculate the area, verify if we have a square from left, diagonal and top. 
        If yes, whatever is the most minimal value of square, we will calculate our area based on that + 1, at current cell and the level. 
        """
        if len(matrix)==0: return 0
        dp = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        res_ = 0
        
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                if matrix[i-1][j-1]=="1":
                    dp[i][j] = 1+min(
                        dp[i-1][j-1] if i>=1 and j>=1 else 0,
                        dp[i-1][j] if i>=1 else 0,
                        dp[i][j-1] if j>=1 else 0
                    )
                    res_ = max(res_, dp[i][j])
        
        return res_*res_