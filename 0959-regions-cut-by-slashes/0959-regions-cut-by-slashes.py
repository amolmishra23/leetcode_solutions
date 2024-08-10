class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        r1, c1 = len(grid), len(grid[0])
        r2, c2 = 3*r1, 3*c1
        grid2 = [[0]*c2 for _ in range(r2)]
        
        for r in range(r1):
            for c in range(c1):
                nr, nc = r*3, c*3
                
                if grid[r][c] == "/":
                    grid2[nr][nc+2] = 1
                    grid2[nr+1][nc+1] = 1
                    grid2[nr+2][nc] = 1
                elif grid[r][c] == "\\":
                    grid2[nr][nc]=1
                    grid2[nr+1][nc+1]=1
                    grid2[nr+2][nc+2]=1
                    
        def dfs(r, c):
            if not 0<=r<r2 or not 0<=c<c2 or not grid2[r][c]==0:
                return 
            grid2[r][c]=1
            for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                dfs(nr, nc)
                
        res = 0
        for i in range(r2):
            for j in range(c2):
                if grid2[i][j]==0:
                    dfs(i, j)
                    res += 1
                    
                    
        return res
        