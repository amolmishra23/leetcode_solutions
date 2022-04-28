class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}
        
        def dfs(i):
            if i in safe: return safe[i]
            
            safe[i] = True
            
            for nei in graph[i]:
                if dfs(nei): return True
                
            safe[i] = False
            # return True
            
        res = []
        for i in range(n):
            if not dfs(i): res.append(i)
                
        return res