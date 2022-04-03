class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for x,y,c in connections:
            graph[x].append((c,y))
            graph[y].append((c,x))
            
        visited = set()
        total = 0
        queue = [(0, 1)]
        
        while queue and len(visited)<n:
            cost, city = heapq.heappop(queue)
            if city not in visited:
                visited.add(city)
                total += cost
                for cost,neigh in graph[city]:
                    if neigh not in visited:
                        heapq.heappush(queue, (cost, neigh))
        
        return total if len(visited)==n else -1
    
    """
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        p = {city:city for city in range(1, n+1)}
        num_comp = n
        
        def find(x):
            if x!=p[x]:
                p[x] = find(p[x])
            return p[x]
        
        def union(x,y):
            nonlocal num_comp
            px,py = find(x), find(y)
            if px==py: return False
            num_comp -= 1
            p[px]=py
            return True
        
        connections.sort(key = lambda x:x[2])
        
        total = 0
        for x,y,c in connections:
            if union(x,y): total+=c
                
        return total if num_comp==1 else -1
    """