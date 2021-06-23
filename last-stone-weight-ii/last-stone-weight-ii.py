class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        def max_subset(nums):
            n, sum_ = len(nums), sum(nums)
            target = sum_//2

            dp = [[None]*(target+1) for _ in range(n+1)]

            for i in range(n+1):
                for j in range(target+1):
                    if i==0 and j==0: dp[i][j] = True
                    elif i==0: dp[i][j] = False
                    elif j==0: dp[i][j] = True
                    elif nums[i-1]<=j: dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                    else: dp[i][j] = dp[i-1][j]

            for i in range(target, -1, -1):
                if dp[n][i]: return i
            
        cache={}
        max_sum = max_subset(stones)
        return sum(stones)-2*max_sum