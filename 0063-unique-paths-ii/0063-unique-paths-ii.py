class Solution:
    def uniquePathsWithObstacles(self, arr: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def solve(m, n):
            if m==x-1 and n==y-1: return 1
            
            if not 0<=m<x or not 0<=n<y or arr[m][n]==1: return 0
            
            return solve(m+1, n) + solve(m, n+1)

        if arr[-1][-1]==1: return 0
        x, y = len(arr), len(arr[0])
        return solve(0,0)