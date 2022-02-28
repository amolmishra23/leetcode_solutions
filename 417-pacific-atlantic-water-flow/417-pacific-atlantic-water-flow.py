class Solution:
    """
    The DFS solution is straightforward. Starting from each point, and dfs its neighbor if the neighbor is equal or less than itself. And maintain two boolean matrix for two oceans, indicating an ocean can reach to that point or not. Finally go through all nodes again and see if it can be both reached by two oceans. The trick is if a node is already visited, no need to visited again. Otherwise it will reach the recursion limits.
    """
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []
        self.dir = [(-1,0),(1,0),(0,-1),(0,1)]
        self.m, self.n = len(matrix), len(matrix[0])
        self.matrix = matrix
        
        pacific = [[False]*self.n for _ in range(self.m)]
        atlantic = [[False]*self.n for _ in range(self.m)]
        
        for i in range(self.m):
            self.dfs(i, 0, pacific, -math.inf)
            self.dfs(i, self.n-1, atlantic, -math.inf)
            
        for i in range(self.n):
            self.dfs(0, i, pacific, -math.inf)
            self.dfs(self.m-1, i, atlantic, -math.inf)
            
        res = []
        for i in range(self.m):
            for j in range(self.n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append((i,j))
        
        return res
    
    def dfs(self, i, j, arr, prev):
        if not 0<=i<self.m or not 0<=j<self.n or arr[i][j] or self.matrix[i][j]<prev: return 
        
        arr[i][j]=1
        
        for x,y in self.dir:
            self.dfs(i+x, j+y, arr, self.matrix[i][j])
            
        
        
        