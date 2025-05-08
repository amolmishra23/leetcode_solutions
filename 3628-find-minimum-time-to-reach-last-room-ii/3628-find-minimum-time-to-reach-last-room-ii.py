class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        heap = [(0,0,0)]
        time = [[float("inf")]*n for _ in range(m)]

        while heap:
            t,r,c = heapq.heappop(heap)
            if t >= time[r][c]: continue
            if r==m-1 and c==n-1: return t
            time[r][c] = t

            for nr,nc in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                if 0<=nr<m and 0<=nc<n and time[nr][nc]==float("inf"):
                    cost = (r+c)%2 + 1
                    start = max(t, moveTime[nr][nc])
                    timeToReach = cost + start
                    heapq.heappush(heap, (timeToReach, nr, nc))

        return -1