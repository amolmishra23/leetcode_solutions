class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        """
        Intuition
        When two ants meet at some point,
        they change their directions and continue moving again.
        But you can assume they don't change direction and keep moving.

        (You don't really know the difference of ants between one and the other, do you?)


        Explanation
        For ants in direction of left, the leaving time is left[i]
        For ants in direction of right, the leaving time is n - right[i]
        """
        # find max on left, and min on right. Worst cases
        # see which takes most time. 
        # finally we return max of them
        return max(max(left or [0]), n-min(right or [n]))