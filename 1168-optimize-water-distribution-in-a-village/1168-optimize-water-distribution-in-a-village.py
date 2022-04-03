class Solution:
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