class Solution:
    """    
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        seen, cost = set(), 0
        graph = defaultdict(dict)
        
        for x, y, c in pipes:
            graph[x][y] = graph[y][x] = min(graph[x].get(y, float('inf')), c)
        
        queue = []
        for home, cost in enumerate(wells, 1): heapq.heappush(queue,(cost, home))
        
        res = 0
        while queue and len(seen)<n:
            c, x = heapq.heappop(queue)
            if x not in seen:
                seen.add(x)
                res += c
                for y,c in graph[x].items():
                    if y not in seen:
                        heapq.heappush(queue, (c,y))
                        
        return res
    """
    
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
        for u, v, w in sorted([[0,i,w] for i, w in enumerate(wells,1)] + pipes, key=lambda x:x[2]):
            if union(u, v):
                cost += w
                undone -= 1
            if not undone:
                break
        return cost