class DSU:
    def __init__(self):
        self.p = {}

    def find(self, x):
        self.p.setdefault(x, x)
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution:
    def latestDayToCross(self, n, m, C):
        dsu = DSU()
        grid = [[1 for _ in range(m)] for _ in range(n)]
        neibs = [[0,1],[0,-1],[1,0],[-1,0]]
        C = [(x-1, y-1) for x, y in C]

        def index(x, y):
            return x * m + y + 1

        for i in range(len(C) - 1, -1, -1):
            x, y = C[i]

            grid[x][y] = 0
            for dx, dy in neibs:
                nx, ny = x+dx, y+dy
                ind = index(nx, ny)
                if 0<=nx<n and 0<=ny<m and grid[x+dx][y+dy] == 0:
                    dsu.union(ind, index(x, y))
            if x == 0:
                dsu.union(0, index(x, y))
            if x == n - 1:
                dsu.union(m*n + 1, index(x, y))

            if dsu.find(0) == dsu.find(m*n + 1):
                return i