class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree, outdegree = Counter(), Counter()
        
        for u,v in pairs:
            graph[u].append(v)
            indegree[v]+=1
            outdegree[u]+=1
            
        start = pairs[0][0]
        
        for node in outdegree:
            if outdegree[node]-indegree[node]==1: 
                start = node; break
                
        route, stk = [], [start]
        
        while stk:
            while graph[stk[-1]]:
                stk.append(graph[stk[-1]].pop())
            route.append(stk.pop())
        
        route.reverse()
        return [[route[i], route[i+1]] for i in range(len(route)-1)]