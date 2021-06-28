class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def solve(i, j, K):
            # we are already out of bounds so condition wont satisfy
            if i<0 or i>n-1 or j<0 or j>n-1: return 0
            
            # we are within the bounds, and have successfully made k as 0. So its a success
            if K==0: return 1
            
            # if we have previously solved for it. 
            if cache[i][j][K] is not None: return cache[i][j][K]
            
            # 8 dirs possible. Each one should be accounted in probability. 
            rate = 0
            for d in dirs:
                # all of them have equal probability of occurence. 
                rate += 0.125*solve(i+d[0], j+d[1], K-1)
                
            cache[i][j][K] = rate
            return rate
            
        
        # writing all the arrows in mathematical form
        dirs= [
            [-2,-1],[-1,-2],
            [2,1],[1,2],
            [2,-1],[1,-2],
            [-2,1],[-1,2]
        ]
        cache=[[[None for _ in range(k+1)] for _ in range(n+1)] for _ in range(n+1)]
        print (cache[n][n][k])
        return solve(row, column, k)
        