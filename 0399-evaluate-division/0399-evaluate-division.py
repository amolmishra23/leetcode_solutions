class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        root = {}
        
        def find(x):
            par, ratio = root.setdefault(x, (x, 1.0))
            if par!=x:
                new_par, new_ratio = find(par)
                root[x] = (new_par, ratio*new_ratio)
            return root[x]
        
        def union(x, y, ratio=None):
            x_par, x_ratio = find(x)
            y_par, y_ratio = find(y)
            if ratio is None:
                return x_ratio/y_ratio if x_par==y_par else -1.0
            if x_par!=y_par:
                root[x_par] = (y_par, y_ratio/x_ratio*ratio)
        
        for (x,y),v in zip(equations, values):
            union(x, y, v)
        
        return [union(x, y) if x in root and y in root else -1.0 for x, y in queries]