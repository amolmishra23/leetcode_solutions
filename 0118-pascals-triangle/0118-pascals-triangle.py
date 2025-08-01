class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        for i in range(1, numRows+1):
            res.append([1]*i)
        
        for i in range(2, numRows):
            for j in range(1,i):
                res[i][j] = res[i-1][j-1]+res[i-1][j]
        
        return res