class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        for u,v,c in edges: self.graph[u].append((v, c))

    def addEdge(self, edge: List[int]) -> None:
        u,v,c = edge; self.graph[u].append((v, c))
        

    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [(0, node1)]
        dist, vis = defaultdict(lambda: float("inf")), set()
        
        while heap:
            curr_dist, curr_node = heapq.heappop(heap)
            if curr_node == node2: return curr_dist
            
            if curr_node in vis: continue
            vis.add(curr_node)
            
            for neigh, n_dist in self.graph[curr_node]:
                if dist[neigh] > curr_dist+n_dist:
                    dist[neigh] = curr_dist+n_dist
                    heapq.heappush(heap, (curr_dist+n_dist, neigh))
                    
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)