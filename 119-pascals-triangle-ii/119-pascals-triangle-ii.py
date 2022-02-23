class Solution:
    def getRow(self, n: int) -> List[int]:
        if n==0: return [1]
        elif n==1: return [1, 1]
        else:
            ans = [[1]*i for i in range(1,n+2)]
        
            for i in range(2, n+1):
                for j in range(1, i):
                    # if we carefully observe the picture, we start adding only from j-1,j columns, in prev row. 
                    ans[i][j] = ans[i-1][j-1]+ans[i-1][j]

            return ans[-1]