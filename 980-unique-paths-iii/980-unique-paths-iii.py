class Solution:
    def dfs(self, x, y, zeros):
        if not 0<=x<self.m or not 0<=y<self.n or self.grid[x][y]==-1:
            return 0
        
        # in case we reached destination and zeros is -1, we can return 1. 
        # else return 0
        # goal is to reach destination how so ever we can
        if self.grid[x][y]==2:
            return 1 if zeros==-1 else 0
        
        # to mark the path as visited and return midway
        self.grid[x][y] = -1
        
        # getting all possible solutions
        temp = self.dfs(x-1, y, zeros-1)+\
                self.dfs(x+1, y, zeros-1) +\
                self.dfs(x, y+1, zeros-1) +\
                self.dfs(x, y-1, zeros-1)
        
        self.grid[x][y] = 0
        return temp
        
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return
        
        self.grid, self.m, self.n = grid, len(grid), len(grid[0])
        x, y, zeros = None, None, 0
        
        # save the start location
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0: zeros += 1
                elif grid[i][j] == 1: x,y = i,j
        
        # start a dfs
        return self.dfs(x, y, zeros)