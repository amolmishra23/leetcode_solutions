class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1]>1 and grid[1][0]> 1: return -1
        
        heap, visited = [(0,0,0)], set()
        m, n = len(grid), len(grid[0])
        
        while heap:
            curr_time, r, c = heapq.heappop(heap)
            if r==m-1 and c==n-1: return curr_time
            
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if not 0<=nr<m or not 0<=nc<n or (nr, nc) in visited: continue
                
                time_diff, new_time = grid[nr][nc] - curr_time, None

                if time_diff>0:
                    if time_diff%2:
                        # in case the difference is odd, we can be sure to reach exactly by target time. 
                        new_time = grid[nr][nc]
                    else:
                        # in case the difference is even for sure we need to have an extra step
                        new_time = grid[nr][nc]+1
                else:
                    # here we just increment curr_time by 1 (as we cannot move backwards in time)
                    new_time = curr_time + 1
                    
                heapq.heappush(heap, (new_time, nr, nc))
                visited.add((nr, nc))
                
        return -1
        