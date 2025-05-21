class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        firstRow, firstCol = False, False

        for j in range(n):
            if matrix[0][j]==0: firstRow=True; break

        for i in range(m):
            if matrix[i][0]==0: firstCol=True; break

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    matrix[i][0]=0; matrix[0][j]=0; 

        # while substituting 0, we ignore the 0th row and 0th col. Else entire matrix might become 0. 
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0

        if firstRow:
            for j in range(n):
                matrix[0][j]=0

        if firstCol:
            for i in range(m):
                matrix[i][0]=0

        return matrix
        