class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Very simple problem. Just maintain the parent to child relationships
        Start from such nodes which have no dependency
        As we traverse the nodes keep reducing the dependency
        In the end if we have traversed all the nodes, we found a right order
        """
        graph, depend_count = defaultdict(list), defaultdict(int)
        result = []
        
        for c,p in prerequisites:
            graph[p].append(c)
            depend_count[c] += 1
        
        sources = deque()
        
        for c in range(numCourses):
            if depend_count[c]==0: sources.append(c)
                
        while sources:
            temp = sources.popleft()
            result.append(temp)
            for c in graph[temp]:
                depend_count[c]-=1
                if depend_count[c]==0: sources.append(c)
                    
        return result if len(result)==numCourses else []