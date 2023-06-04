class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        par = {i:i for i in range(n)}
        size = {i:1 for i in range(n)}
        
        def find(x):
            if par[x]!=x:
                par[x] = find(par[x])
            return par[x]
        
        def union(x, y):
            par_x, par_y = find(x), find(y)
            if par_x==par_y: return False
            if size[par_x] > size[par_y]:
                par[par_y] = par_x
                size[par_x]+=size[par_y]
            else:
                par[par_x] = par_y
                size[par_y]+=size[par_x]
        
        for i in range(n):
            for j in range(n):
                if i!=j and isConnected[i][j]:
                    union(i, j)

        res = sum(k==v for k,v in par.items())
        return res
                    