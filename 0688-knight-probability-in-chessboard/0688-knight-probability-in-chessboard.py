class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dirs = [
            (-2,-1), (-2,1),(2, 1), (2,-1),
            (-1, -2), (-1, 2),(1,2), (1, -2)
        ]
        
        @lru_cache(None)
        def solve(i, j, k):
            if not 0<=i<n or not 0<=j<n: return 0
            if k==0: return 1            
            return sum(0.125*solve(i+x, j+y, k-1) for x, y in dirs)
        
        return solve(row, column, k)