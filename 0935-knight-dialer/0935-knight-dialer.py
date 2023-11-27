class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = (10**9)+7
        ans = 0
        cache = [[[None]*(n+1) for _ in range(3)] for _ in range(4)]
        
        # @lru_cache(None)
        def paths(i, j, n):
            if i<0 or j<0 or i>=4 or j>=3 or (i==3 and j!=1): return 0
            if n==1: return 1
            if cache[i][j][n]!=None: return cache[i][j][n]
            
            res = 0
            res = (res + paths(i-1, j-2, n-1)) % MOD
            res = (res + paths(i-2, j-1, n-1)) % MOD
            res = (res + paths(i+1, j+2, n-1)) % MOD
            res = (res + paths(i+2, j+1, n-1)) % MOD
            res = (res + paths(i-1, j+2, n-1)) % MOD
            res = (res + paths(i+2, j-1, n-1)) % MOD
            res = (res + paths(i+1, j-2, n-1)) % MOD
            res = (res + paths(i-2, j+1, n-1)) % MOD
            
            cache[i][j][n] = res
            return res
        
        for i in range(4):
            for j in range(3):
                ans = (ans + paths(i, j, n))%MOD
        
        return ans