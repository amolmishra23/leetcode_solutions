class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        root = {}
        
        """
        equations = [["a","b"],["b","c"]], values = [2.0,3.0]
        after 1st equation, we have par[a]=b. ratio[a]=2
        after 2nd equation, we have par[b]=c, ratio[b]=3
        
        when we need to find from a to b, in union find way we go from a=>b and then b=>c
        multiply the respective ratio's. 2*3. hence answer is 6.
        
        As we do find, we also do path compression, and keep multiplying our ratio with parent ratio for the same reason.
        After the path compression, we will have par[a]=c, ratio[a]=6
        par[b]=c, ratio[b]=3
        
        if to convert from a to b. we will basically do 6//3 = 2. 
        
        If no of queries are high, this approach is best suited because
        we will be able to answer in almost O(1), once the graph is created and compressed. 
        """
        def find(x):
            xp, xr = root.setdefault(x, (x, 1.0))
            if x!=xp:
                tp, tr = find(xp)
                root[x] = (tp, xr*tr)
            return root[x]
        
        def union(x, y, ratio):
            xp, xr, yp, yr = *find(x), *find(y)
            if not ratio:
                return xr/yr if xp==yp else -1.0
            if xp!=yp:
                root[xp] = (yp, yr/xr*ratio)
                
        for (x,y),v in zip(equations, values):
            union(x, y, v)
            
        return [union(x,y,0) if x in root and y in root else -1.0 for x,y in queries]