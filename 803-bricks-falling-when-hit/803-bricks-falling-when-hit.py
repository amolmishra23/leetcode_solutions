class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1]*n
        
    def find(self, i):
        if i==self.parents[i]: return i
        self.parents[i] = self.find(self.parents[i])
        return self.parents[i]
    
    def union(self, p, q):
        root_p, root_q = map(self.find, (p, q))
        if root_p == root_q: return
        small, big = sorted([root_p, root_q], key = lambda x: self.sizes[x])
        self.parents[small]=big
        self.sizes[big]+=self.sizes[small]
    
    def top(self):
        return self.sizes[
            self.find(len(self.sizes)-1)
        ]
        
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def index(C, r, c): # here C is no of rows/columns. If the index is (2,3) and n is 5, meaning index in 1d array would be 2*5+3 = 13
            return r*C+c
        
        # All the 4 directions to be traversed
        directions = [
            (0, -1), (-1, 0), (0, 1), (1, 0)
        ]
        R, C = len(grid), len(grid[0])
        
        # We make a clone of original grid, 
        hit_grid = [row[:] for row in grid]
        
        # In the clone graph, make all the hit spots as 0 (like they never existed)
        for i, j in hits:
            hit_grid[i][j] = 0
        
        # Construct a union find matrix, with 1 more slot(to hold union of all the roof elements). 
        uf = UnionFind(R*C+1)
        
        """
        Iterating over the hit_grid(Doesnt include the actual hits), we try to see if any brick, has any adjacent bricks. We try to make them as 1 component using the union find. 
        If the row is 0, means its rooftop, so we directly add it to the roof component
        """
        for r, row in enumerate(hit_grid):
            for c, val in enumerate(row):
                if not val: continue
                if r==0: uf.union(index(C, r, c), R*C)
                if r and hit_grid[r-1][c]: uf.union(index(C, r, c), index(C, r-1, c))
                if c and hit_grid[r][c-1]: uf.union(index(C, r, c), index(C, r, c-1))
        
        result = []
        """
        We iterate over the hits in reverse
        If there was no brick at hit location, ignore.
        if there was brick at hit location, we do a union around, making them all under same component. 
        If its a 0th row, means its root component. Add it to roof component
        Finally make the hit_grid of that hit location as 1 for future purposes.
        We find the curr_roof-prev_roof-1. 1 is for hit location. And append this to result array
        
        Return the result reversed array
        """
        for r, c in reversed(hits):
            prev_roof = uf.top()
            if grid[r][c]==0: result.append(0); continue
            for x, y in directions:
                nr, nc = r+x, c+y
                if 0<=nr<R and 0<=nc<C and hit_grid[nr][nc]:
                    uf.union(index(C, r, c), index(C, nr, nc))
            if r==0:
                uf.union(index(C, r, c), R*C)
            hit_grid[r][c]=1
            result.append(max(0, uf.top()-prev_roof-1))
        
        return result[::-1]
            
        
        