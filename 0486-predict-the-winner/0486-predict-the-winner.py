class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def solve(l, r):
            if l==r: return nums[l]
            return max(nums[l] - solve(l+1, r), nums[r] - solve(l, r-1))
        return solve(0, len(nums)-1) >= 0