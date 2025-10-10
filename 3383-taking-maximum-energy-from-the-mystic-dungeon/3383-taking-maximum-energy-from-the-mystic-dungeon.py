class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = energy.copy()
        n = len(energy)

        for i in range(n-k-1, -1, -1):
            dp[i] += dp[i+k]

        return max(dp)