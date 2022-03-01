class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if (not grid or len(grid)==0 or len(grid[0])==0): return 0
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    res += 4
                    # subtracting one for grid[i][j] and one for grid[i-1][j]
                    # perimeter only intends to include the common edges per se. 
                    if i>0 and grid[i-1][j]==1: res-=2
                    if j>0 and grid[i][j-1]==1: res-=2
                        
        return res