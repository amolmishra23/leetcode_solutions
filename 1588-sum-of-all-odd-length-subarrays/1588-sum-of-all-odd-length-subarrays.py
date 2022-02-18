class Solution:
    def sumOddLengthSubarrays(self, A: List[int]) -> int:
        res, n = 0, len(A)
        for i, a in enumerate(A):
            res += ((i + 1) * (n - i) + 1) // 2 * a
        return res