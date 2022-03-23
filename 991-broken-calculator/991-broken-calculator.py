class Solution:
    """
    So we check only the last bit of Y, since doubling and -1 can only alter (directly) one bit.

    if last bit of Y is 0, the last operation must be doubling, we trace back to Y/2
    if last bit of Y is 1, the last operation must be decrement, we trace back to Y+1
    """
    def brokenCalc(self, x: int, y: int) -> int:
        if x>=y: return x-y
        return 1+(self.brokenCalc(x, y+1) if y&1 else self.brokenCalc(x, y//2))