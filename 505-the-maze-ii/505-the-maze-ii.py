class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], dest: List[int]) -> int:
        m, n, q, visited = len(maze), len(maze[0]), [(0, start[0], start[1])], {(start[0], start[1]): 0}
        
        while q:
            dist, x, y = heapq.heappop(q)
            if x==dest[0] and y==dest[1]: return dist
            
            for dx, dy in [(1,0), (-1,0),(0,1),(0,-1)]:
                nx, ny, d = x, y, 0
                
                while 0<=nx+dx<m and 0<=ny+dy<n and maze[nx+dx][ny+dy]!=1:
                    nx+=dx
                    ny+=dy
                    d += 1
                    
                if (nx, ny) not in visited or visited[(nx, ny)] > dist+d:
                    visited[(nx, ny)] = dist+d
                    heapq.heappush(q, (dist+d, nx, ny))
                    
        return -1