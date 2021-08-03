class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # referred to the following video: https://www.youtube.com/watch?v=_426VVOB8Vo
        # we do a basic dfs and mark all the islands(basically name them as 2,3,4,5 and have their count)
        # now at every possible 0, we try to put 1, and see if we are intersecting multiple islands. 
        # if multiple islands, we add up all their sizes. And the biggest size is returned as the answer. 
        def dfs(i, j, curr):
            if i>=m or j>=n or i<0 or j<0 or grid[i][j]!=1: return 0
            
            grid[i][j] = curr
            return 1+dfs(i+1, j, curr)+dfs(i-1, j, curr)+dfs(i, j+1, curr)++dfs(i, j-1, curr)
            
        if not grid or len(grid)==0: return 0
        
        max_, island_id = 0, 2
        map_ = {}
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    temp = dfs(i, j, island_id)
                    max_ = max(max_, temp)
                    map_[island_id] = temp
                    island_id +=1
        
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    set_ = set()
                    for dir_ in dirs:
                        x,y=dir_[0]+i, dir_[1]+j
                        if 0<=x<m and 0<=y<n and grid[x][y]!=0:
                            set_.add(grid[x][y])
                            
                    sum_ = 1
                    
                    for num in set_: sum_+=map_[num]
                    
                    max_ = max(max_, sum_)
                    
        return max_