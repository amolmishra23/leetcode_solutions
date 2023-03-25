class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.size = defaultdict(lambda: 1)
        self.total = (n*(n-1))//2
        
    def find(self, x):
        self.parent.setdefault(x, x)
        if self.parent[x]==x: return self.parent[x]
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px==py: return False
        self.total -= (self.size[px]*self.size[py])
        if self.size[px] > self.size[py]:
            self.parent[py]=px
            self.size[px]+=self.size[py]
        else:
            self.parent[px]=py
            self.size[py]+=self.size[px]
            
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for x,y in edges: uf.union(x,y)
        return uf.total