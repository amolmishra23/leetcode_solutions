class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        
        in_degree = [0]*n
        
        pres = [set() for _ in range(n)]
        
        for a,b in prerequisites:
            graph[a] += b,
            in_degree[b] += 1
            pres[b].add(a)
            
        queue = deque([course for course, degree in enumerate(in_degree) if degree==0])
        
        while queue:
            pre = queue.popleft()
            
            for course in graph[pre]:
                pres[course] |= pres[pre]
                in_degree[course]-=1
                if in_degree[course]==0: queue.append(course)
                    
        return [pre in pres[course] for pre, course in queries ]