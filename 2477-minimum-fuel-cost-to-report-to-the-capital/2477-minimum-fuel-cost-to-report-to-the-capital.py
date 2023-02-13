class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph, self.res = defaultdict(list), 0
        
        for a,b in roads:
            graph[a].append(b)
            graph[b].append(a)
            
        def dfs(curr, parent):
            count = 1
            
            for neigh in graph[curr]:
                if neigh==parent: continue
                count += dfs(neigh, curr)
                
            if curr!=0:
                self.res += ceil(count/seats)
            
            return count
        
        dfs(0,-1)
        return self.res