class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res, stk = 0, [0]

        for num in nums:
            while stk and stk[-1] > num:
                stk.pop()

            if not stk or stk[-1] < num:
                res += 1
                stk.append(num)

        return res
