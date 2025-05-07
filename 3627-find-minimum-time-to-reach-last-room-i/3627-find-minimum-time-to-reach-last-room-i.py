class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        dp = [[float("inf")]*n for _ in range(m)]
        heap = [(0,0,0)]

        while heap:
            dis, r, c = heapq.heappop(heap)
            print(dis, r, c)
            if dis >= dp[r][c]: continue
            if r==m-1 and c==n-1: return dis

            dp[r][c] = dis

            for nr, nc in [[r+1, c], [r-1,c], [r,c+1], [r,c-1]]:
                if 0<=nr<m and 0<=nc<n and dp[nr][nc]==float("inf"):
                    nDis = max(moveTime[nr][nc], dis) + 1
                    heapq.heappush(heap, (nDis, nr, nc))

        return -1