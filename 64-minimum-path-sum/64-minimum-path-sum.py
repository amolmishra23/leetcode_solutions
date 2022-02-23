class Solution:
    def minPathSum(self, arr: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def solve(m, n):
            if m==x-1 and n==y-1: return arr[m][n]
            
            # Must for outer paths to be invalid.
            # hence return them as infinite, to not be considered
            if not 0<=m<x or not 0<=n<y: return float('inf')
            
            return arr[m][n]+min(solve(m+1, n), solve(m, n+1))

        x, y = len(arr), len(arr[0])
        return solve(0,0)