class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for i, j in dislikes:
            graph[i].append(j)
            graph[j].append(i)
            
        color = {}
        
        def dfs(node, c=0):
            if node in color: 
                return color[node]==c
            color[node]=c
            for neigh in graph[node]:
                if not dfs(neigh, c^1): return False
            return True
        
        for node in range(1, n+1):
            if node not in color:
                if not dfs(node): return False
                
        return True