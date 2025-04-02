class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res, n = 0, len(nums)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    res = max(res, (nums[i] - nums[j]) * nums[k])

        return res