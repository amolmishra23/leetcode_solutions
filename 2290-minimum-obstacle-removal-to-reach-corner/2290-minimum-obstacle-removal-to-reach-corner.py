class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        minHeap, visited = [(0,0,0)], set([(0, 0)])
        
        while minHeap:
            obs, r, c = heapq.heappop(minHeap)
            if (r,c) == (m-1, n-1): return obs
            
            nei = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            for nr, nc in nei:
                if 0<=nr<m and 0<=nc<n and (nr,nc) not in visited:
                    heapq.heappush(minHeap, (obs+grid[nr][nc], nr, nc))
                    visited.add((nr, nc))
            
        return -1