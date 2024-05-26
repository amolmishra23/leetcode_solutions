class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = (10**9)+7

        dp = [[[None for _ in range(3)] for _ in range(2)] for _ in range(n+1)]

        @lru_cache(None)
        def solve(i, absent, late):
            if dp[i][absent][late]: 
                return dp[i][absent][late]

            if i>=n: return 1
            
            # when student was present
            res = solve(i+1, absent, 0)
            
            # when student was absent
            if absent == 0:
                res += solve(i+1, 1, 0)

            # when student was late
            if late < 2:
                res += solve(i+1, absent, late+1)

            dp[i][absent][late] = res % MOD
            return dp[i][absent][late]

        return solve(0, 0, 0)