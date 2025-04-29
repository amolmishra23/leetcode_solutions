class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, count, res = 0, 0, 0
        target = max(nums)

        for r in range(len(nums)):
            count += (nums[r]==target)
            while count>=k:
                res += (n-r)
                count -= (nums[l]==target)
                l += 1

        return res