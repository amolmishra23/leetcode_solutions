class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][0]==1 or grid[-1][-1]==1: return -1
        
        q = deque([(0,0)])
        dist = 1
        
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                if x==m-1 and y==n-1: return dist
                for dx in range(-1,2):
                    for dy in range(-1,2):
                        if dx==0 and dy==0: continue
                        nx, ny = x+dx, y+dy
                        if not 0<=nx<m or not 0<=ny<n or grid[nx][ny]==1: continue
                        grid[nx][ny] = 1
                        q.append((nx, ny))
            dist += 1
        
        return -1