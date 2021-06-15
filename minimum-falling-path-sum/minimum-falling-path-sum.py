class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        m, n = len(arr), len(arr[0])
        res = float('inf')
        cache={}
        
        def solve(arr, i, j):
            if (i,j) in cache: return cache[(i,j)]
            
            if i==m or j==n: return 0
            
            opt = []
            
            if 1<=j<=n-1:
                opt.append(solve(arr, i+1, j-1))
            
            opt.append(solve(arr, i+1, j))
            
            if 0<=j<=n-2:
                opt.append(solve(arr, i+1, j+1))
                
            cache[(i,j)] = arr[i][j] + min(opt)
            return cache[(i,j)]
        
        for x in range(n):
            res = min(res, solve(arr, 0, x))
        
        return res