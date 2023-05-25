class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        dp = [1] + [0] * (k + min(maxPts - 1,n))
        s = 0
        for i in range(1, k + min(maxPts,n)):
            if i <= k: s = s + dp[i - 1] / maxPts
            if i - maxPts - 1 >= 0: s -= dp[i - maxPts - 1] / maxPts
            dp[i] = s

        return sum(dp[k:n + 1])