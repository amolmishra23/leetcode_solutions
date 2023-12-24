class Solution:
    def minOperations(self, s: str) -> int:
        res = sum(ch!=str(i%2) for i, ch in enumerate(s))
        return min(res, len(s)-res)