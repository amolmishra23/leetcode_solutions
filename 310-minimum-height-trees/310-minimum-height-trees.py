class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Topological sorting.
        The graph which has most dependencies, if that becomes root node. We tend to have that much less levels. 
        """
        graph = {i:[] for i in range(n)}
        indegree = {i:0 for i in range(n)}
        
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
            indegree[x]+=1
            indegree[y]+=1
            
        q = deque()
        for i in range(n):
            if indegree[i]==1: 
                q.append(i)
        
        temp = []
        
        while q:
            curr_len=len(q)
            temp = []
            for _ in range(curr_len):
                curr_node = q.popleft()
                temp.append(curr_node)
                for neigh in graph[curr_node]:
                    indegree[neigh]-=1
                    if indegree[neigh]==1: q.append(neigh)
                        
        if n==1: temp.append(0)
        return temp
        
            