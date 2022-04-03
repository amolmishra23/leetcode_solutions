class Solution(object):
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        dist = [[float('inf')] * n for _ in range(m)]
        minHeap = [(0, 0, 0)] # distance, row, col
        DIR = [0, 1, 0, -1, 0]
        while minHeap:
            d, r, c = heappop(minHeap)
            
            # we had entered this in heap by mistake. ignore it, as dist[r][c] has a better value
            if d > dist[r][c]: continue
            
            # if we reached destination return
            if r == m - 1 and c == n - 1:
                return d  # Reach to bottom right
            
            # expanding across all the neighbours
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                
                # for all valid neighbours, update them in the queue
                # and also store them in heap, to expand in future. 
                if 0 <= nr < m and 0 <= nc < n:
                    newDist = max(d, abs(heights[nr][nc] - heights[r][c]))
                    
                    # only insert in heap, if new dist is any smaller than prev distances
                    if dist[nr][nc] > newDist:
                        dist[nr][nc] = newDist
                        heappush(minHeap, (dist[nr][nc], nr, nc))