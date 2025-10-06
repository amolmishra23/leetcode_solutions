class Solution:
    def dfs(self, i, j, arr, prev):
        if not 0<=i<self.m or not 0<=j<self.n or arr[i][j] or self.heights[i][j]<prev: return 
        
        arr[i][j] = 1
        
        for m,n in zip(self.dir[:-1], self.dir[1:]): 
            self.dfs(i+m, j+n, arr, self.heights[i][j])
        
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.dir = [0,1,0,-1,0]
        self.m, self.n = len(heights), len(heights[0])
        self.heights = heights
        
        pacific = [[0]*self.n for _ in range(self.m)]
        atlantic = [[0]*self.n for _ in range(self.m)]
        
        for i in range(self.m):
            self.dfs(i, 0, pacific, -math.inf)
            self.dfs(i, self.n-1, atlantic, -math.inf)
        
        for j in range(self.n):
            self.dfs(0, j, pacific, -math.inf)
            self.dfs(self.m-1, j, atlantic, -math.inf)
            
        res = []
        for i in range(self.m):
            for j in range(self.n):
                if pacific[i][j] and atlantic[i][j]: res.append((i, j))
                    
        return res
        
        
        