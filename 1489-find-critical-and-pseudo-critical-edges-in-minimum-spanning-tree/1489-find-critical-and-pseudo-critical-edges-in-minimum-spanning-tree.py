class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.weight = 0
        self.count = 0
        
    def find(self, x):
        if x!=self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y, w):
        r1 = self.find(x)
        r2 = self.find(y)
        
        if r1!=r2:
            self.parents[r2]=r1
            self.weight += w
            self.count += 1
        
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [(w, a, b, i) for i, (a,b,w) in enumerate(edges)]
        edges.sort()
        
        uf1 = UnionFind(n)
        for w,a,b,_ in edges: uf1.union(a,b,w)
        ce, pce = [], []
        
        minWeight = uf1.weight
        
        for i in range(len(edges)):
            uf2 = UnionFind(n)
            for j in range(len(edges)):
                if i==j: continue
                w, a, b, _ = edges[j]
                uf2.union(a, b, w)
                
            if uf2.weight>minWeight or uf2.count<n-1: ce.append(edges[i][3])
            else:
                uf3 = UnionFind(n)
                w,a,b,_ = edges[i]
                uf3.union(a,b,w)
                for j in range(len(edges)):
                    w,a,b,_ = edges[j]
                    uf3.union(a,b,w)
                
                if uf3.weight==minWeight:
                    pce.append(edges[i][3])
                    
        return ce, pce
                
            
        