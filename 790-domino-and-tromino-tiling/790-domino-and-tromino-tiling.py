"""
Only understable video to this question: https://www.youtube.com/watch?v=CecjOo4Zo-g
If not so good at math, and solve it using a programming intuition. 

These are all the possible cases using which we can recursively fill our 2xn grid. We have two different cases where 
previous rows have no gaps and where previous rows do have gaps. We need to treat them different as that affects the 
choices of our tiles. So to sum up, we have -

No Previous Gaps:
===================
Place T1 and move to i+1: solve(i+1, previousGap=false)
Place T2 in pair and move to i+2: solve(i+2, previousGap=false)
Place either T3 or T4 (consider both cases) and move to i+2 with gap at i+1th column: 2*solve(i+2, previousGap=true)

Previous Gaps Present:
=====================
Place T5 or T6 & fill previous gap (consider only 1 bcoz depending on current configuration, only 1 grid out of them will fit) and move to i+1 with no previous gaps remaining: solve(i+1, previousGap=false)
Place T2 & fill previous gap and move to i+1 with gap present in ith column: solve(i+1, previousGap=true)
That's it! We now just recursively fill the grid using above cases. If we reach the end of the grid (column i = n) with no previous gaps, then we know that we found 1 possible way of tiling grid, so we return 1. Otherwise if we exceed bounds of grid or reach end with previous gaps remaining, then we return false.
"""
class Solution:
    def numTilings(self, n):
        @lru_cache(None)
        def solve(i, gap):
            if i>n: return 0
            if i==n: return 1 if not gap else 0
            if gap:
                return solve(i+1, False)+solve(i+1, True)
            # we multiply by 2, because we have tried both things here. T3 and T4. To consider it as 2 cases. 
            return solve(i+1, False)+solve(i+2, False)+2*solve(i+2, True)
        
        return solve(0, False) % 1_000_000_007