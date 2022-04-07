class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        queue = [(grid[0][0], 0, 0)]
        res = float('-inf')
        n = len(grid)
        seen = set()
        
        
        while queue:
            c, x, y = heapq.heappop(queue)
            res = max(res, c)
            if x==y==n-1: return res
            
            for i, j in ((x+1,y), (x-1,y),(x,y+1),(x,y-1)):
                if 0<=i<n and 0<=j<n and (i,j) not in seen:
                    seen.add((i,j))
                    heapq.heappush(queue, (grid[i][j], i, j))