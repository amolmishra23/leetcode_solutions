class Solution:
    def findPoisonedDuration(self, ts: List[int], d: int) -> int:
        # in an ideal world the res would be:
        res = len(ts)*d
        
        # but that there could be overlappings.
        # to overcome the overlappings, the trick is:
        """
        [1,4] with duration 2 means
        2-(4-1) = 2-3 = -1. So we subtract 0, and no effetc
        
        [1,2] with duration 2 means
        2-(2-1) = 2-1 = 1. So we subtract 1, and effect is there. 
        """
        for i in range(1, len(ts)):
            res -= max(0, d-(ts[i]-ts[i-1]))
            
        return res
        