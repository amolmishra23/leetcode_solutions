class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # if not matrix or not matrix[0]: return matrix
        
        m, n = len(matrix), len(matrix[0])
        
        zero_first_row = any(matrix[0][i]==0 for i in range(n))
        zero_first_col = any(matrix[i][0]==0 for i in range(m))
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
        
        if zero_first_row: 
            for i in range(n): matrix[0][i]=0
        if zero_first_col: 
            for i in range(m): matrix[i][0]=0
                
        return matrix