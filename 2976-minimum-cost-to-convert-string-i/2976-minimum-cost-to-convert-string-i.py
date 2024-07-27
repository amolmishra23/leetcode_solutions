class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        alphabet = string.ascii_lowercase
        graph = defaultdict(lambda: inf)
        
        for a, b, c in zip(original, changed, cost): 
            graph[a, b] = min(graph[a, b], c)
        
        for char, a, b in product(alphabet, alphabet, alphabet):
            graph[a, b] = min(graph[a, b], graph[a, char] + graph[char, b])
        
        ans = sum(table[a, b] for a, b in zip(source, target) if a != b)
        return ans if ans != inf else -1
    
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)
        
        for u,v,c in zip(original, changed, cost):
            graph[u].append((v, c))
            
        def dijkstra(u, v):
            visited=set()
            heap=[(0, u)]
            
            while heap:
                dis, curr = heapq.heappop(heap)
                if curr in visited:
                    continue
                visited.add(curr)
                if curr==v: return dis
                
                for neigh, ndis in graph[curr]:
                    heapq.heappush(heap, (dis+ndis, neigh))
                    
            return -1
        
        orig_list, chan_list = list(set(original)), list(set(changed))
        cost = defaultdict(dict)
        for u in orig_list:
            for v in chan_list:
                cost[u][u]=cost[v][v]=0
                if dijkstra(u, v)!=-1:
                    cost[u][v]=dijkstra(u, v)
                
        res = []
        for u,v in zip(source,target):
            if u in cost and v in cost[u]: res.append(cost[u][v])
            else: return -1
            
        return sum(res)
        