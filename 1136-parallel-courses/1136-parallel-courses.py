class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        in_degree = {i:0 for i in range(1,n+1)}
        graph = {i:[] for i in range(1,n+1)}
        
        for x,y in relations:
            graph[x].append(y)
            in_degree[y]+=1
            
        sources = deque([c for c,v in in_degree.items() if v==0])
        sem, res = 0, 0
        
        while sources:
            curr_len = len(sources)
            sem += 1
            
            for _ in range(curr_len):
                curr = sources.popleft()
                res += 1
                for neigh in graph[curr]:
                    in_degree[neigh]-=1
                    if in_degree[neigh]==0: sources.append(neigh)
                    
        return sem if res==n else -1