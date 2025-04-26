class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        start, kMinIdx, kMaxIdx = 0, -1, -1

        for i in range(len(nums)):
            if not minK <= nums[i] <= maxK:
                start, kMinIdx, kMaxIdx = i+1, -1, -1
            
            if nums[i]==minK: kMinIdx = i
            if nums[i]==maxK: kMaxIdx = i

            res += max(0, min(kMinIdx, kMaxIdx) - start + 1)

        return res