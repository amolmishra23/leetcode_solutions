class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = Counter()

        l, res, pairs = 0, 0, 0

        for r in range(len(nums)):
            pairs += count[nums[r]]
            count[nums[r]] += 1

            while pairs>=k:
                res += (len(nums)-r)
                count[nums[l]]-=1
                pairs -= count[nums[l]]
                l += 1

        return res            

