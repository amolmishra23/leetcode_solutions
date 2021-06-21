class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        m, n = len(arr), len(arr[0])
        res = float('inf')
        cache={}
        
        def solve(arr, i, j):
            if (i,j) in cache: return cache[(i,j)]
            
            # if we have reached the end, we can return 0, as no more path
            if i==m or j==n: return 0
            
            # we can only travel. left, center, right. Trying all the 3 options.n 
            opt = []
            
            # left
            if 1<=j<=n-1:
                opt.append(solve(arr, i+1, j-1))
            
            # middle
            opt.append(solve(arr, i+1, j))
            
            # right
            if 0<=j<=n-2:
                opt.append(solve(arr, i+1, j+1))
                
            # we anyways need to add the value at the node
            cache[(i,j)] = arr[i][j] + min(opt)
            return cache[(i,j)]

        # Starting from each possible index in the row0, to see which one fetches us the minimum.
        for x in range(n):
            res = min(res, solve(arr, 0, x))
        
        return res