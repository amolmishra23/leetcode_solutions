from copy import deepcopy

class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        """
        Number of zeros, we can easily find using number of 2, 5
        So in prefix sum way, for all 4 directions we need to find the number of 2,5
        up, down, left, right
        
        Now as we find the result, we can find 4 types. 
        up-right, up-left, down-right, down-left. 
        We need to subtract the curr-idx we iterating, as thats added 2 times. 
        Finally number of zeros is only min count of 2,5. That also needed to be accounted. 
        """ 
        @lru_cache(None)
        def factors(x):
            res = [0,0]
            while x%2==0:
                res[0]+=1
                x//=2
            while x%5==0:
                res[1]+=1
                x//=5
            return res
        
        def sum_factors(x, y):
            return [x[0]+y[0], x[1]+y[1]]
        
        def diff_and_min(x, y):
            return min(x[0]-y[0], x[1]-y[1])
        
        m, n = len(grid), len(grid[0])
        zeros = [[None for _ in range(n)] for _ in range(m)]
        up, down, left, right =  deepcopy(zeros), deepcopy(zeros), deepcopy(zeros),deepcopy(zeros)
        
        for i in range(m):
            for j in range(n):
                up[i][j] = factors(grid[i][j]) if i == 0 else sum_factors(up[i-1][j], factors(grid[i][j]))
                left[i][j] = factors(grid[i][j]) if j == 0 else sum_factors(left[i][j-1], factors(grid[i][j]))
                
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                down[i][j] = factors(grid[i][j]) if i==m-1 else sum_factors(down[i+1][j], factors(grid[i][j]))
                right[i][j] = factors(grid[i][j]) if j==n-1 else sum_factors(right[i][j+1], factors(grid[i][j]))
                
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(
                    res,
                    diff_and_min(sum_factors(up[i][j], right[i][j]), factors(grid[i][j])),
                    diff_and_min(sum_factors(up[i][j], left[i][j]), factors(grid[i][j])),
                    diff_and_min(sum_factors(down[i][j], right[i][j]), factors(grid[i][j])),
                    diff_and_min(sum_factors(down[i][j], left[i][j]), factors(grid[i][j]))
                )
                
        return res