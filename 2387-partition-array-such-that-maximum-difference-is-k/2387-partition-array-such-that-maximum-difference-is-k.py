class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        currMin = nums[0]
        for num in nums[1:]:
            if num-currMin > k:
                res += 1
                currMin = num

        return res