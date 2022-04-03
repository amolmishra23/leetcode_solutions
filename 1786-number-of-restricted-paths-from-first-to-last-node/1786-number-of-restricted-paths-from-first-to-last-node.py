class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        if n==1: return 0
        g = defaultdict(list)
        
        for u, v, w in edges:
            g[u].append((w,v))
            g[v].append((w,u))
            
        def dijkstra():
            heap = [(0,n)]
            distances = [float('inf')]*(n+1)
            distances[n] = 0
            
            while heap:
                d, u = heapq.heappop(heap)
                if d!=distances[u]: continue
                
                for w,v in g[u]:
                    if distances[v] > distances[u]+w:
                        distances[v] = distances[u]+w
                        heapq.heappush(heap, (distances[v], v))
                        
            return distances
        
        @lru_cache(None)
        def dfs(start):
            if start==n: return 1
            res = 0
            
            for _, nei in g[start]:
                if distances[nei]<distances[start]:
                    res = (res + dfs(nei)) % (10**9+7)
            
            return res
        
        distances = dijkstra()
        return dfs(1)