"""
just need to check if an elem == (i-1, j-1)
As soon as we find its not, we return False
"""
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        for row in range(m):
            for col in range(n):
                if row>0 and col>0 and matrix[row][col] != matrix[row-1][col-1]: return False
                
        return True