class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def topo(curr, visited):
            if curr in visited: return visited[curr]
            
            visited[curr] = True
            
            for neigh in graph[curr]:
                if topo(neigh, visited): return True
            
            visited[curr] = False
        
        visited, res = {}, []
        for i in range(len(graph)):
            if not topo(i, visited): res.append(i)
            
        return res