class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        p = [0.0]*n
        p[start] = 1.0
        heap = [(-p[start], start)]
        
        g = defaultdict(list)
        for i, (a,b) in enumerate(edges):
            g[a].append((b, i))
            g[b].append((a, i))
        
        while heap:
            prob, node = heapq.heappop(heap)
            if p[node]<prob: continue
            if node==end: return -prob
                
            for neigh, idx in g[node]:
                if -prob*succProb[idx]>p[neigh]:
                    p[neigh] = -prob*succProb[idx]
                    heapq.heappush(heap, (-p[neigh], neigh))
            
        return 0.0