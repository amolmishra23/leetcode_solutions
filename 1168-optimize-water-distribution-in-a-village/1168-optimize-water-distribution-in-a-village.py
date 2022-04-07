class Solution:
    def minCostToSupplyWater1(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        seen, cost = set(), 0
        graph = defaultdict(dict)
        
        for x,y,c in pipes:
            graph[x][y] = graph[y][x] = min(graph[x].get(y, float('inf')), c)
            
        queue = []
        for i, well in enumerate(wells, 1):
            heapq.heappush(queue, (well, i))
            
        while queue and len(seen)<n:
            c, x = heapq.heappop(queue)
            if x not in seen:
                seen.add(x)
                cost += c
                for y,c in graph[x].items():
                    if y not in seen:
                        heapq.heappush(queue, (c, y))
        
        return cost
    
    def minCostToSupplyWater(self, n, wells, pipes):
        p = list(range(n+1))

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                p[py] = px
                return True
            return False

        cost, undone = 0, n
        
        # adding imaginary 0 node. 0 to ith node, cost of setting welling is w. 
        # so we either set up well. Or traverse to that node. 
        for u, v, w in sorted([[0,i,w] for i, w in enumerate(wells,1)] + pipes, key=lambda x:x[2]):
            if union(u, v):
                cost += w
                undone -= 1
            if not undone:
                break
        return cost