class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        diff, res = start ^ goal, 0
        while diff:
            res += diff & 1
            diff >>= 1
            
        return res
    
        # return sum(start & (1<<i) != goal & (1<<i) for i in range(max(start.bit_length(), goal.bit_length())))