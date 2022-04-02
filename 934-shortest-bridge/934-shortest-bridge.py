class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        found = False
        m, n = len(grid), len(grid[0])
        queue = deque()
        dirs = [(1,0), (-1,0),(0,1),(0,-1)]
        
        isvalid = lambda i,j: 0<=i<m and 0<=j<n and grid[i][j]==1
        
        def dfs(i, j):
            nonlocal queue
            if isvalid(i, j):
                grid[i][j]=2
                
                queue.append((i, j))
                
                for x,y in dirs:
                    dfs(i+x, j+y)
                
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    dfs(i, j)
                    found = True
                    break
            if found: break
                
        level = 0
        
        while queue:
            curr_count = len(queue)
            
            for _ in range(curr_count):
                x,y = queue.popleft()
                
                for dx,dy in dirs:
                    nx, ny = x+dx, y+dy
                    
                    if not 0<=nx<m or not 0<=ny<n or grid[nx][ny]==2: continue
                        
                    if grid[nx][ny]==1: return level

                    grid[nx][ny]=2
                    queue.append((nx,ny))
            level += 1
            
        return -1
                        