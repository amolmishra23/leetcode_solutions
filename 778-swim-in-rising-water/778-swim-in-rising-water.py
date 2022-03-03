class UF:
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1]*n
        
    def find(self, x):
        if self.parents[x]==x: return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        par_x, par_y = map(self.find, [x,y])
        if par_x==par_y: return 
        small, big = sorted([par_x, par_y], key = lambda x: self.size[x])
        self.parents[small] = big
        self.size[big] += self.size[small]

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = UF(n**2)
        rev_map = [None]*(n**2)
        
        for i in range(n):
            for j in range(n):
                rev_map[grid[i][j]] = (i, j)
        
        allowed = [(-1,0),(1,0),(0,1),(0,-1)]
        
        for i in range(n**2):
            x,y = rev_map[i]
            for dx,dy in allowed:
                nx,ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<n and grid[nx][ny]<=i:
                    uf.union(x*n+y, nx*n+ny)
                    if uf.find(0)==uf.find(n**2-1): return i
                    
        return n**2-1                    