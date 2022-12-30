class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(curr, path):
            if curr==len(graph)-1:
                res.append(list(path))
            else:
                for neigh in graph[curr]: dfs(neigh, path+[neigh])
        
        res = []
        dfs(0, [0])
        return res