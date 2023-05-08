class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        
        diag1 = sum(mat[i][i] for i in range(n))
        diag2 = sum(mat[i][n-1-i] for i in range(n))
        
        return diag1 + diag2 - (mat[n//2][n//2] if n%2 else 0)