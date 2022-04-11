class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        Dont get confused in the long problem description. 
        As mentioned from the examples, we basically pick the last element and make it as 1st element of 2d matrix with every shift operation. 
        In order to optimized do it, imagine this array to be a 1d matrix and perform the same. 
        We keep doing %n so that not to go over board
        """
        m, n = len(grid), len(grid[0])
        
        ans = [[0]*n for _ in range(m)]
        
        k %= m*n
        
        for i in range(m):
            for j in range(n):
                # converting it into 1d index. 
                # doing its mod, to not exceed the limits. 
                
                # i*n+j and add k to it
                # now mod it with m*n
                index = (i*n+j+k)%(m*n)
                x=index//n
                y=index%n
                ans[x][y] = grid[i][j]
                
        return ans