class Solution:
    def minPartitions(self, n: str) -> int:
        return max([int(k) for k in str(n)])