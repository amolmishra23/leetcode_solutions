class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0
        
        for row in range(m):
            for col in range(n):
                if matrix[row][col]!=0 and row>0:
                    matrix[row][col] += matrix[row-1][col]
                    
            curr_row = sorted(matrix[row], reverse=True)
                
            for i in range(n):
                res = max(res, curr_row[i]*(i+1))
                    
        return res