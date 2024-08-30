class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        MAX_DIST = 990000000
        def djikstra(u, v):
            heap, visited = [(0,u)], set()
            
            while heap:
                d, curr = heapq.heappop(heap)
                if curr==v: return d
                if curr in visited: continue
                visited.add(curr)
                
                for neigh, ndist in graph[curr]:
                    if neigh not in visited and ndist!=-1:
                        heapq.heappush(heap, (d+ndist, neigh))
                        
            return MAX_DIST
                
        graph=defaultdict(list)
        
        for u,v,d in edges:
            if d!=-1:
                graph[u].append((v,d))
                graph[v].append((u,d))
            
        curr_dist = djikstra(source, destination)
        if curr_dist<target: return []
        
        for i, (u,v,d) in enumerate(edges):
            if d!=-1: continue
            
            if curr_dist == target:
                edges[i][2] = MAX_DIST
                continue
                
            edges[i][2] = 1
            graph[u].append((v, 1)); graph[v].append((u, 1))
            
            curr_dist = djikstra(source, destination)
            if curr_dist <= target:
                edges[i][2] += (target-curr_dist)
                curr_dist = target
                
        return edges if curr_dist==target else []
            