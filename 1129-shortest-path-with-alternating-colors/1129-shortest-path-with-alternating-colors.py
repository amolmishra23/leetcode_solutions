class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda: defaultdict(set))
        red, blue = 0, 1
        for u, v in redEdges:
            graph[u][red].add(v)
        for u, v in blueEdges:
            graph[u][blue].add(v)
        res = [math.inf]*n
        q = deque([(0,red), (0, blue)])
        level = -1
        while q:
            level += 1
            for _ in range(len(q)):
                node, color = q.popleft()
                target_color = color^1
                neighs = graph[node][target_color]
                res[node] = min(res[node], level)
                for neigh in list(neighs):
                    graph[node][target_color].remove(neigh)
                    q.append((neigh, target_color))
                    
        return [r if r!=math.inf else -1 for r in res]
        
        