class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        par = {}
        
        def find(x):
            par.setdefault(x, x)
            if par[x]!=x:
                par[x]=find(par[x])
            return par[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px==py: return False
            par[px]=py
            return True
        
        for x,y in edges: union(x,y)
        
        return find(source)==find(destination)