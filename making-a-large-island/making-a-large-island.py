class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid or len(grid)==0: return 0
        m, n = len(grid), len(grid[0])
        
        # @functools.lru_cache(None)
        def dfs(i, j, curr):
            if not 0<=i<m or not 0<=j<n or grid[i][j]!=1: return 0
            
            grid[i][j]=curr
            
            return 1+dfs(i+1, j, curr)+dfs(i-1, j, curr)+dfs(i, j+1, curr)+dfs(i, j-1, curr)
        
        res, index = 0, 2
        count = {}
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    temp = dfs(i, j, index)
                    res = max(res, temp)
                    count[index] = temp
                    index+=1

        dir_ = [[1,0], [-1,0], [0,1], [0,-1]]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    s = set()
                    for d in dir_:
                        x, y = i+d[0], j+d[1]
                        if 0<=x<m and 0<=y<n and grid[x][y]!=0:
                            s.add(grid[x][y])
                        
                    curr_count = 1
                    for x in s: curr_count += count[x]
                        
                    res = max(res, curr_count)
                    
        return res
                        