class Solution:
    """
    Whole idea is, 1 person should reach from 0,0 to n, n. And come back to 0,0 picking up maximum cherries.
    Obviously, solution is through recursion.
    A dp optimization could be, 2 people going from 0,0 to n, n. simulating both onward and return. check for all the paths. whoever gives maximum is our solution.
    """
    @functools.lru_cache(None)
    def solve(self, r1, c1, r2, c2):
        if r1>=self.m or r2>=self.m or c1>=self.n or c2>=self.n or self.grid[r1][c1]==-1 or self.grid[r2][c2]==-1:
            return float('-inf')
        
        if r1==self.m-1 and c1==self.n-1:
            return self.grid[r1][c1]
        
        if r2==self.m-1 and c2==self.n-1:
            return self.grid[r2][c2]
        
        res = 0
        # at same point, we can just pick 1 cherry. 
        if r1==r2 and c1==c2: res+=self.grid[r1][c1]
        else: res+=(self.grid[r1][c1]+self.grid[r2][c2])
        
        p1 = self.solve(r1+1, c1, r2+1, c2)
        p2 = self.solve(r1+1, c1, r2, c2+1)
        p3 = self.solve(r1, c1+1, r2+1, c2)
        p4 = self.solve(r1, c1+1, r2, c2+1)
        
        res += max(p1, p2, p3, p4)
        return res
        
    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.grid, self.m, self.n = grid, len(grid), len(grid[0])
        return max(self.solve(0,0,0,0), 0)