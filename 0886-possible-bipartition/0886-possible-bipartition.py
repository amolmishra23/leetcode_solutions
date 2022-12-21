class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for x, y in dislikes:
            graph[x].append(y)
            graph[y].append(x)
            
        visited = {}
        def dfs(node, c=0):
            if node in visited: return visited[node]==c
            
            visited[node] = c
            
            for neigh in graph[node]:
                if not dfs(neigh, c^1): return False
            
            return True
        
        for node in range(1, n+1):
            if node not in visited:
                if not dfs(node): return False
                
        return True