class Solution:
    def dfs(self, x, y, zeros):
        if not 0<=x<self.m or not 0<=y<self.n or self.grid[x][y]==-1:
            return 0
        
        if self.grid[x][y]==2:
            return 1 if zeros==-1 else 0
        
        
        self.grid[x][y] = -1
        
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
        
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0: zeros += 1
                elif grid[i][j] == 1: x,y = i,j
        
        return self.dfs(x, y, zeros)