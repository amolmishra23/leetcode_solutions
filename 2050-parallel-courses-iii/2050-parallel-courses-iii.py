class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph=defaultdict(list)
        indegree=Counter()
        
        for i,j in relations:
            i-=1; j-=1
            graph[i].append(j)
            indegree[j]+=1
            
        dist = [0]*n
        sources = deque()
        for i in range(n):
            if indegree[i]==0:
                sources.append(i)
                dist[i] = time[i]
                
        while sources:
            curr = sources.popleft()
            
            for neigh in graph[curr]:
                dist[neigh] = max(dist[neigh], dist[curr]+time[neigh])
                indegree[neigh]-=1
                if indegree[neigh]==0: sources.append(neigh)
                    
        return max(dist)
        