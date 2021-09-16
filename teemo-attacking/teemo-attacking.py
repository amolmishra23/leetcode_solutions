class Solution:
    def findPoisonedDuration(self, ts: List[int], d: int) -> int:
        # in an ideal world the res would be:
        res = len(ts)*d
        
        # but that there could be overlappings.
        # to overcome the overlappings, the trick is:
        for i in range(1, len(ts)):
            res -= max(0, d-(ts[i]-ts[i-1]))
            
        return res
        