class DSUF:
    def __init__(self, row):
        self.roots = dict()
        for x in row: 
            if x%2!=0: self.roots[x] = x-1
            else: self.roots[x] = x
    
    def union(self, u, v):
        p1 = self.find(u)
        p2 = self.find(v)
        
        if p1==p2: return
        
        self.roots[p1] = p2
    
    def find(self, u):
        if self.roots[u]==u: return u
        self.roots[u] = self.find(self.roots[u])
        return self.roots[u]
    
    def disjoint_sets(self):
        return len(
            set(self.find(p) for p in self.roots)
        )
    

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        dsuf = DSUF(row)
        
        for i in range(0, n, 2):
            dsuf.union(row[i], row[i+1])
        
        disjoint_sets = dsuf.disjoint_sets()
        return n//2 - disjoint_sets
        