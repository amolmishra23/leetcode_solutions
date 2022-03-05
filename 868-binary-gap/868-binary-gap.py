class Solution:
    def binaryGap(self, n: int) -> int:
        result, last = 0, None
        for i in range(32):
            if n>>i & 1:
                if last is not None:
                    result = max(result, i-last)
                last = i
        return result
            