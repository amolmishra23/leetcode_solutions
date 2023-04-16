class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """
        Water==0, land==1
        We need to find such a water cell, which is farthest from the land cell.
        For this, we can go from each water cell, and do BFS, and whatever is highest number is our solution.
        Or we come in reverse way, via multi-source BFS. Start from all the land cells at once, and keep doing BFS as farthest as possible. Once we have exhausted our BFS queue, that is the farthest water cell <-> land cell ka distance. Is our solution
        """
        q, steps = deque(), 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # multi source bfs from all the neighbours of land cell
                if grid[i][j]==1: q.extend([(i-1,j),(i+1,j),(i,j-1),(i,j+1)])
            
        while q:
            steps += 1
            for _ in range(len(q)):
                i,j = q.popleft()
                # from the water cell, we will keep expanding across all the water cells possible. 
                # finally when we reach farthest water cell that is our answer.  
                if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]==0:
                    grid[i][j]=steps
                    q.extend([(i-1,j),(i+1,j),(i,j-1),(i,j+1)])
        
        return -1 if steps==1 else steps-1