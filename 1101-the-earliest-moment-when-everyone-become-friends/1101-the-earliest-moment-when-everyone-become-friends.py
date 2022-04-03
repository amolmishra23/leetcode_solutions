class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.size[px] < self.size[py]:
            self.parent[px] = self.parent[py]
            self.size[py] += self.size[px]
        else:
            self.parent[py] = self.parent[px]
            self.size[px] += self.size[py]
            
        return True

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        root = list(range(n))
        
        def find(x):
            if x!=root[x]:
                root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px==py: return 0
            root[px] = py
            return True
        
        def component_count():
            val = set(map(find, root))
            return len(val)
        
        last_ts = None
        logs.sort(key=lambda x: x[0])
        
        for last_ts, a, b in logs:
            union(a, b)
            if component_count()==1: return last_ts
                    
        return -1