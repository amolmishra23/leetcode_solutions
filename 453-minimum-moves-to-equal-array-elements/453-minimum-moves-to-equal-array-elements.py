class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mi = min(nums)
        ans = 0
        for x in nums:
            ans += x - mi
        return ans