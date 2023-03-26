class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        res = -1
        # to mark if a node is visited or not
        # this persists across the dfs travel
        visited = {}
        # dist records number of nodes we traversed to reach it
        # the lifetime of this is only the cycle of dfs
        dist = {}
        
        def dfs(x):
            nonlocal res, visited, dist
            if x not in visited:
                if x in dist:
                    res = max(res, len(dist) - dist[x])
                elif edges[x]!=-1:
                    dist[x] = len(dist)
                    dfs(edges[x])
                    dist.pop(x)
                visited[x]=True
                
        for i in range(len(edges)): dfs(i)
            
        return res
                