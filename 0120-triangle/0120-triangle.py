class Solution:
    def minimumTotal(self, arr: List[List[int]]) -> int:
        @lru_cache(None)
        def solve(i, j):
            if i==len(arr): return 0
            
            return arr[i][j] + min(solve(i+1, j), solve(i+1, j+1))
        
        return solve(0, 0)
        