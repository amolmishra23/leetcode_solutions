class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.size = [0] * n
    def isExist(self, u):
        return self.parent[u] >= 0
    def add(self, u):
        if self.isExist(u): return  # Only add if not existed yet!
        self.parent[u] = u
        self.size[u] = 1
    def find(self, u):
        if self.parent[u] == u: return u
        self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False
        if self.size[pu] <= self.size[pv]:  # Merge the smaller component to the bigger component
            self.parent[pu] = pv  # Merge u into v
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu  # Merge v into u
            self.size[pu] += self.size[pv]
        return True

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        DIR = [0, 1, 0, -1, 0]
        m, n, ans = len(grid), len(grid[0]), 0
        uf = UnionFind(m * n)

        def landNeighbors(r, c):
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                neiId = nr * n + nc
                if nr < 0 or nr == m or nc < 0 or nc == n or not uf.isExist(neiId): continue
                yield neiId

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0: continue
                curId = r * n + c
                uf.add(curId)
                for neiId in landNeighbors(r, c):
                    uf.union(curId, neiId)
                p = uf.find(curId)
                ans = max(ans, uf.size[p])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1: continue
                neiParents = set()
                for neiId in landNeighbors(r, c):
                    neiParents.add(uf.find(neiId))
                sizeFormed = 1  # Start with 1, which is matrix[r][c] when turning from 0 into 1
                for p in neiParents:
                    sizeFormed += uf.size[p]
                ans = max(ans, sizeFormed)
        return ans