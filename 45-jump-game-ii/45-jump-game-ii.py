class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        N = len(nums)

        def dp(index):
            if index >= N - 1:
                return 0

            if index in memo:
                return memo[index]

            min_jump = math.inf
            for i in range(1, nums[index] + 1):
                min_jump = min(min_jump, 1 + dp(index + i))
                memo[index] = min_jump

            return min_jump
        return dp(0)