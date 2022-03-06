class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res, cols = 0, len(grid[0])
        
        for row in grid:
            c=cols-1
            while c>=0 and row[c]<0: c-=1
            res += cols-1-c
        
        return res