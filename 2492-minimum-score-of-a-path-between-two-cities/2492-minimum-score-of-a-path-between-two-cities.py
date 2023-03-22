class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for x,y,z in roads: graph[x][y]=graph[y][x]=z
        
        q, visited, res = deque(), set(), float("inf")
        q.append(1)
        
        while q:
            curr = q.popleft()
            
            for neigh, dis in graph[curr].items():
                if neigh not in visited: 
                    visited.add(neigh); q.append(neigh)
                res = min(res, dis)
        
        return res
        
            
            