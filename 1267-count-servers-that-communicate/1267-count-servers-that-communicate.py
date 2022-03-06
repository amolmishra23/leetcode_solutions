class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        res, m, n = 0, len(grid), len(grid[0])
        row, col = [0]*m, [0]*n
        
        for i in range(m):
            for j in range(n):
                # increment row and col count
                if grid[i][j]:
                    row[i]+=1
                    col[j]+=1
                    
        for i in range(m):
            for j in range(n):
                # to check if connection is there in network
                if grid[i][j] and (row[i]>1 or col[j]>1):
                    res+=1
        
        return res