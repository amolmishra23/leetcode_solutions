class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for x in arr: dp[x] = 1 + dp[x-difference]
        return max(dp.values())
                