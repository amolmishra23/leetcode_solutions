class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # idea is to return true, as soon as we find a cycle. 
        # condition for graph to be tree is, no cycles, and we should have visited all nodes starting from one node. 
        def dfs(node, visited, parent):
            if node in visited: return visited[node]
            
            visited[node]=True
            
            for neigh in graph[node]:
                if neigh==parent: continue
                if dfs(neigh, visited, node): return True
            
            visited[node] = False
            
        graph = defaultdict(list)
        
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        visited = {}
        has_cyle = dfs(0, visited, -1)
        if has_cyle: return False
        
        return len(visited)==n