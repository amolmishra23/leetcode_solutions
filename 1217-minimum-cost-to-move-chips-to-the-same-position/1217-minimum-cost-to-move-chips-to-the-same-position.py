"""
The key observation here is that it's free to move a chip from an even number to another even number, and it is free to move a chip from an odd number to another odd number. It only costs to move an even to an odd, or an odd to an even. Therefore, we want to minimise such moves.
"""

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even_pos = sum(x%2==0 for x in position)
        return min(even_pos, len(position)-even_pos)