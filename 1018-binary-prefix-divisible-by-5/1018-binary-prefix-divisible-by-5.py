class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res, rem = [], 0

        for num in nums:
            rem = ((rem<<1)+num)%5
            res.append(rem%5==0)

        return res