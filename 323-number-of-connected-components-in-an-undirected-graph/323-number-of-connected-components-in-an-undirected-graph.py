class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n
        
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px==py: return False
        if self.size[px]<self.size[py]:
            self.parent[px] = py
            self.size[py] += self.size[px]
        else:
            self.parent[py] = px
            self.size[px] += self.size[py]
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        res = n
        
        for a, b in edges:
            if uf.union(a,b): res -= 1
            
        return res