class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = Counter()
        queue = deque()
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
            
        for i in range(numCourses): 
            if indegree[i]==0: queue.append(i)
               
        visited=0
        while queue:
            curr = queue.popleft()
            visited += 1
            for neigh in graph[curr]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    queue.append(neigh)
            
        return visited==numCourses
            
        
        