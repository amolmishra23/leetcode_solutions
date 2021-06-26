class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def solve(max_move, i, j):
            # cant move anywhere else
            if max_move<0: return 0
            
            # we just managed to step out, so valid path and return 1
            if i>=m or j>=n or i<0 or j<0: return 1
            
            if (i,j,max_move) in dp: return dp[(i,j,max_move)]
            
            res = 0
            res+=solve(max_move-1, i-1,j)
            res+=solve(max_move-1, i+1,j)
            res+=solve(max_move-1, i,j-1)
            res+=solve(max_move-1, i,j+1)
            
            dp[(i,j,max_move)] = res
            return res
            
        
        const = (10**9)+7
        dp = {}
        return solve(maxMove, startRow, startColumn)%const
