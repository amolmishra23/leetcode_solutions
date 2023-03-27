class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @lru_cache(None)
        def solve(x, y):
            if not 0<=x<len(grid) or not 0<=y<len(grid[0]): return float("inf")
            if x==len(grid)-1 and y==len(grid[0])-1: return grid[x][y]
            return grid[x][y] + min(solve(x+1,y), solve(x, y+1))
        
        return solve(0, 0)