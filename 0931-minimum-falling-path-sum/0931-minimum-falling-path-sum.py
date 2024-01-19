class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        m, n = len(arr), len(arr[0])
        
        @lru_cache(None)
        def solve(i, j):
            if not 0<=j<n: return float("inf")
            if i==m or j==n: return 0
            return arr[i][j] + min(solve(i+1, nj) for nj in range(j-1, j+2))

        return min(solve(0,x) for x in range(n))
