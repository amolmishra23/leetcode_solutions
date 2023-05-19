class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        par = {}
        
        def find(x):
            par.setdefault(x, x)
            if par[x]!=x:
                par[x] = find(par[x])
            return par[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px==py: return False
            par[px]=py
            return True
        
        for idx, nodes in enumerate(graph):
            for node in nodes:
                if find(idx)==find(node): return False
                union(nodes[0], node)
                
        return True