class Solution:
    def getRow(self, n: int) -> List[int]:
        if n==0: return [1]
        elif n==1: return [1,1]
        else:
            # res = [[1]*i for i in range(1, n+2)]
            res = []
            for i in range(1, n+2):
                res.append([1]*i)
            
            for i in range(2, n+1):
                for j in range(1, i):
                    res[i][j] = res[i-1][j-1]+ res[i-1][j]
                    
            return res[-1]