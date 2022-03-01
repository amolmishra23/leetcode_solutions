class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        
        diagonals = [[] for _ in range(m+n-1)]
        
        for i in range(m):
            for j in range(n):
                diagonals[i+j].append(mat[i][j])
                
        res = diagonals[0]
        
        for x in range(1, len(diagonals)):
            if x%2==1:
                res.extend(diagonals[x])
            else:
                res.extend(diagonals[x][::-1])
                
        return res