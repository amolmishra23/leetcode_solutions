class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(dict)
        
        for s,d,t in times:
            graph[s][d] = t
            
        heap = [(0, k)]
        visited = {k: 0}
        seen = set()
        res = float('-inf')
        
        while heap:
            curr_time, curr_node = heapq.heappop(heap)
            if curr_node in seen: continue
            res = max(res, curr_time)
            seen.add(curr_node)
            if len(seen)==n: return res
            
            for neigh, t in graph[curr_node].items():
                if neigh not in visited or visited[neigh]>curr_time+t:
                    visited[neigh] = curr_time+t
                    heapq.heappush(heap, (curr_time+t, neigh))
        
        return -1