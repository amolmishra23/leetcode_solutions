class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        """
        return min([z for _,_,z in roads])
        above code passes 38/41 cases. Where it fails is, when we find min edge in another disconnected component.
        So the goal is start from 1, and howsoever the graph extends, find minimum edge in this entire component.,
        going long route is totally okay. find the min score. 
        """
        graph = defaultdict(dict)
        for x,y,z in roads: graph[x][y]=graph[y][x]=z
        
        q, visited, res = deque(), set(), float("inf")
        q.append(1)
        
        # No need to check if we reached final dest or not. 
        # Because problem spec has specified at least one path there
        # Even if we reached final dest, still travel all routes 
        # in hope of finding a minimum score, and only then return
        while q:
            curr = q.popleft()
            
            for neigh, dis in graph[curr].items():
                if neigh not in visited: 
                    visited.add(neigh); q.append(neigh)
                res = min(res, dis)
        
        return res
        
            
            