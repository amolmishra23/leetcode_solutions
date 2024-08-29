class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        par = {}
        
        def find(x):
            par.setdefault(x, x)
            if par[x]!=x:
                par[x] = find(par[x])
            return par[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px==py: return False
            par[px] = py
            return True
        
        for r,c in stones: union(r, c+100000)
        return len(stones) - len({find(a) for a in par.keys()})