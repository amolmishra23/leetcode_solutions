class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        
        # finding min most element each row wise
        # finding max most element each col wise
        row = list(map(min, matrix))
        col = list(map(max, zip(*matrix)))
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==row[i]==col[j]: res.append(matrix[i][j])
        
        return res