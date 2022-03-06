class Solution:
    def shortestPath(self, grid, k):
        m, n = len(grid), len(grid[0])
        # start, x, y, k
        Q, v = deque([(0, 0, 0, k)]), set()
        
        # if k is bigger than total nodes
        if k >= m + n - 2: return m + n - 2
        
        # Performing BFS
        while Q:
            steps, x, y, k = Q.popleft()
            if (x, y) == (n-1, m-1): return steps
            
            for dx, dy in (x, y-1), (x, y+1), (x-1, y), (x+1, y):
                if 0 <= dx < n and 0 <= dy < m and k - grid[dy][dx] >= 0:
                    new = (dx, dy, k - grid[dy][dx])
                    if new not in v:
                        v.add(new)
                        Q.append((steps + 1, *new))
            
        return -1