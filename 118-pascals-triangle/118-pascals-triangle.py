class Solution:
    def generate(self, n: int) -> List[List[int]]:
        """
        1
        1 1
        1 2 1
        1 3 3 1
        1 4 6 4 1
        
        ans(2, 1) = ans(1, 0)+ans(1, 1)
        """
        ans = [[1]*i for i in range(1,n+1)]
        
        """
        We only need to start filling from the 2nd row
        Filling logic is basically we need to pick from the previous row, j-1 and jth indexes
        """
        for i in range(2, n):
            for j in range(1, i):
                # if we carefully observe the picture, we start adding only from j-1,j columns, in prev row. 
                ans[i][j] = ans[i-1][j-1]+ans[i-1][j]
        
        return ans