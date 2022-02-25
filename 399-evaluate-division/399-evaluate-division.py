import collections

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        Basic dfs problem
        We store all the connections and weights in dict form { a: { b: c}}. a is from node, b is to node, c is distance. 
        Store it like (a,b,c) and (b,a,1/c)
        We need to traverse from a to x via dfs, and find the result and return client. 
        We have a visited set, which keeps track of dfs. And we find the result as chain multiplication and return to client. 
        """
        graph = collections.defaultdict(dict)
        
        for (x,y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1.0/val
        
        def dfs(x, y, visited):
            if x not in graph or y not in graph: return -1.0
            
            if y in graph[x]: return graph[x][y]
            
            for k in graph[x]:
                if k not in visited:
                    visited.add(k)
                    temp = dfs(k, y, visited)
                    if temp==-1: continue
                    else:
                        return graph[x][k] * temp
            
            return -1.0
                    
        res = []
        for query in queries:
            res.append(dfs(query[0], query[1], set()))
            
        return res