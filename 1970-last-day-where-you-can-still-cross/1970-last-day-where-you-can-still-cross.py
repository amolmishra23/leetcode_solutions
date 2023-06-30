class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution:
    def latestDayToCross(self, n, m, C):
        row, col = len(C), len(C[0])
        dsu = DSU(m*n + 2)
        grid = [[1] * m for _ in range(n)]
        neibs = [[0,1],[0,-1],[1,0],[-1,0]]
        C = [(x-1, y-1) for x, y in C]

        def index(x, y):
            return x * m + y + 1

        for i in range(len(C) - 1, -1, -1):
            x, y = C[i][0], C[i][1]

            grid[x][y] = 0
            for dx, dy in neibs:
                ind = index(x+dx, y+dy)
                if x+dx>=0 and x+dx<n and y + dy >= 0 and y + dy < m and grid[x+dx][y+dy] == 0:
                    dsu.union(ind, index(x, y))
            if x == 0:
                dsu.union(0, index(x, y))
            if x == n - 1:
                dsu.union(m*n + 1, index(x, y))

            if dsu.find(0) == dsu.find(m*n + 1):
                return i