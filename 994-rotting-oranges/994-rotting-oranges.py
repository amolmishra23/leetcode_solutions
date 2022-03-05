class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return -1
        
        m, n = len(grid), len(grid[0])
        
        rotten, fresh_count = deque(), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2: rotten.append((i,j))
                elif grid[i][j]==1: fresh_count += 1
        
        itr = 0
        
        while rotten and fresh_count:
            itr += 1
            
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                
                for dx,dy in ((-1,0), (1,0), (0,-1), (0,1)):
                    xx, yy = x+dx, y+dy
                    if not 0<=xx<m or not 0<=yy<n: continue
                    
                    if grid[xx][yy] == 1:
                        fresh_count -= 1
                        rotten.append((xx,yy))
                        grid[xx][yy] = 2
        
        return itr if fresh_count==0 else -1