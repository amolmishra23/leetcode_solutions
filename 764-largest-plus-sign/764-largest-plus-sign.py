class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        """
        A tricky question
        We need to find the biggest + sign we can make with the 1st in the n*n grid. 
        It matters whichever is the smallest side. (square shaped + sign)
        Ideally we could do it with the help of 4 grids, but we can also do using one, if we keep finding the min. 
        """
        
        # set each of them to max value of n
        grid = [[n]*n for _ in range(n)]
        
        # only at mines making them as 0
        for i, j in mines:
            grid[i][j]=0
            
        # traversing all directions to get the best possible
        for i in range(n):
            l,r,u,d=0,0,0,0
            
            # j, k are iterating the columns and rows
            # in to and fro direction
            # so we can avoid multiple traversals. 
            for j,k in zip(range(n), reversed(range(n))):
                l = l+1 if grid[i][j]!=0 else 0
                grid[i][j] = min(grid[i][j], l)
                
                r = r+1 if grid[i][k]!=0 else 0
                grid[i][k] = min(grid[i][k], r)
                
                d = d+1 if grid[j][i]!=0 else 0
                grid[j][i] = min(grid[j][i], d)
                
                u = u+1 if grid[k][i]!=0 else 0
                grid[k][i] = min(grid[k][i], u)
                
        res = 0
        
        # max size plus sign we can get. 
        for i in range(n):
            for j in range(n):
                res = max(res, grid[i][j])
                
        return res