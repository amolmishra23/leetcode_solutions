class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(lambda: 1)
        
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i]-nums[j]
                idx = (i, diff)
                dp[idx] = dp[(j, diff)] + 1
        
        return max(dp.values())