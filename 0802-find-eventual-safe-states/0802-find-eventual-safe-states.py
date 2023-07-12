class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        rev_graph = defaultdict(list)
        out_degree = defaultdict(int)
        q, res = deque(), []
        
        for i in range(len(graph)):
            out_degree[i] = len(graph[i])
            if out_degree[i]==0: q.append(i)
            for neigh in graph[i]:
                rev_graph[neigh].append(i)
        
        while q:
            curr = q.popleft()
            res.append(curr)
            
            for node in rev_graph[curr]:
                out_degree[node] -=1
                if out_degree[node]==0:
                    q.append(node)
        
        return sorted(res)