class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.steps = ""
        distinct_islands = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    self.helper(grid,i,j,"o")
                    distinct_islands.add(self.steps)
                    self.steps = ""
                    
        return len(distinct_islands)
    
    def helper(self, grid, i, j, direct):
        if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]==1:
            self.steps += direct
            grid[i][j] = 0
            self.helper(grid, i+1, j, "d")
            self.helper(grid, i-1, j, "u")
            self.helper(grid, i, j+1, "r")
            self.helper(grid, i, j-1, "l")
            
            self.steps += "b"