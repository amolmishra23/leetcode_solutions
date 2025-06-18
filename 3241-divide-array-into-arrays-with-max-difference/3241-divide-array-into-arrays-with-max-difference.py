class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()

        res = []

        for i in range(0, len(nums), 3):
            a, b, c = nums[i], nums[i+1], nums[i+2]

            if c-a > k: return []

            res.append((a,b,c))

        return res