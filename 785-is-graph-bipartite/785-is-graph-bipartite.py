class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        par, sz = {}, defaultdict(lambda: 1)
        
        def find(x):
            par.setdefault(x, x)
            if x!=par[x]:
                par[x] = find(par[x])
            return par[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px==py: return False
            if sz[px]>sz[py]:
                par[py] = px
                sz[px] += sz[py]
            else:
                par[px] = py
                sz[py] += sz[px]
            return True
        
        for idx, nodes in enumerate(graph):
            for node in nodes:
                if find(idx) == find(node): return False
                union(nodes[0], node)
                
        return True