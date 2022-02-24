class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        """
        Complex variant of the prefix sum problem
        Assuming matrix ends at index i,j we have the sum until then stored in dp
        Now in case we start at a,b. We will just subtract the necessary sums. And get the required sum
        Instead of recomputing all the sums
        """
        if not matrix or not matrix[0]: return
        
        m, n = len(matrix), len(matrix[0])
        self.dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                # because i-1,j-1 are put 2 times through both the i-1,j and i,j-1. 
                # We need to subtract 1 instance of it. 
                self.dp[i][j] = self.dp[i-1][j] + \
                                self.dp[i][j-1] - \
                                self.dp[i-1][j-1] + \
                                matrix[i-1][j-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1] - \
                self.dp[row1][col2+1] - \
                self.dp[row2+1][col1] + \
                self.dp[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)