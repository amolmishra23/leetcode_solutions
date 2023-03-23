class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1: return -1
        par, count, components = {}, defaultdict(lambda: 1), n
        
        def find(x):
            par.setdefault(x, x)
            if par[x]==x: return par[x]
            par[x] = find(par[x])
            return par[x]
        
        def union(x, y):
            nonlocal components
            px, py = find(x), find(y)
            if px==py: return False
            if count[py]>count[px]:
                par[px]=py; count[py]+=count[px]
            else:
                par[py]=px; count[px]+=count[py]
            components -= 1
            return True
        
        extra_connections = 0
        for x,y in connections: 
            if not union(x,y): extra_connections+=1
        
        return components-1 if extra_connections>=components-1 else -1