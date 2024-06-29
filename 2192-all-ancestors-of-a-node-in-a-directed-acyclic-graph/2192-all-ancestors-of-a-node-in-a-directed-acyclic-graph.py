class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegree, graph = [0]*n, defaultdict(set)
        
        for parent,kid in edges:
            graph[parent].add(kid)
            indegree[kid]+=1
            
        dq = deque([u for u, degree in enumerate(indegree) if degree==0])
        
        ans = [set() for _ in range(n)]
        while dq:
            parent = dq.popleft()
            for kid in graph[parent]:
                ans[kid].add(parent)
                ans[kid].update(ans[parent])
                indegree[kid]-=1
                if indegree[kid]==0: dq.append(kid)
                    
        return [sorted(s) for s in ans]
            