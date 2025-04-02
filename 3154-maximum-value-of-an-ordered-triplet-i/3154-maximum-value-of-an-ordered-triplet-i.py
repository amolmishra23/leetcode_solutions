class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        left = nums[0]

        for j in range(1, n):
            left = max(left, nums[j])
            if left==nums[j]: continue
            for k in range(j+1, n):
                res = max(res, (left - nums[j]) * nums[k])

        return res