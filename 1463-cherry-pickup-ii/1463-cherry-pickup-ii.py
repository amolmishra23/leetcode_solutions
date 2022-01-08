class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @functools.lru_cache(None)
        def dfs(r, c1, c2):
            if r==m: return 0
            
            ans = 0
            cherry = grid[r][c1] if c1==c2 else grid[r][c1]+grid[r][c2]
            
            # totally we have 3 possible moves, for every c
            # c-1, c, c+1
            
            for nc1 in range(c1-1, c1+2):
                for nc2 in range(c2-1, c2+2):
                    if 0<=nc1<n and 0<=nc2<n:
                        # as we are proceeding to the next row
                        ans = max(ans, dfs(r+1, nc1, nc2))
            
            return ans+cherry
            
        return dfs(0, 0, n-1)