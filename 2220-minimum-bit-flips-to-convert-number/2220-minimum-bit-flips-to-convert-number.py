class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return sum(start & (1<<i) != goal & (1<<i) for i in range(max(start.bit_length(), goal.bit_length())))