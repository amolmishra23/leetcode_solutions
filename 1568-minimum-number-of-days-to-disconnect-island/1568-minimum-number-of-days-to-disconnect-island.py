class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(graph, i, j):
            if not 0<=i<m or not 0<=j<n or graph[i][j]!=1:
                return
            graph[i][j]=0
            for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                dfs(graph, ni, nj)
                
        def count_islands(graph):
            count = 0
            for i in range(m):
                for j in range(n):
                    if graph[i][j]==1:
                        count += 1; dfs(graph, i, j)  
            return count
        
        if count_islands(deepcopy(grid))!=1: 
            return 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    grid[i][j]=0
                    if count_islands(deepcopy(grid)) != 1:
                        return 1
                    grid[i][j]=1
                    
        return 2