class UF:
    def __init__(self):
        self.par={}
        self.count={}

    def find(self, x):
        self.par.setdefault(x, x)
        if self.par[x]!=x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px==py: return False
        elif px<py:
            self.par[py]=px
        else:
            self.par[px]=py

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UF()
        for c1,c2 in zip(s1, s2): uf.union(c1,c2)
        return "".join([uf.find(x) for x in baseStr])
            