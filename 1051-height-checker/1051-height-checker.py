import collections

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = collections.Counter(heights)
        res, h = 0, 1
        
        # because we are lazy to not sort stuff
        # and do via O(n), we will go this way
        # just keep reducing count[h] when we pass that. Else keep incrementing the res.
        for x in heights:
            while count[h]==0: h+=1
            if x!=h: res+=1 # (no of heights at wrong position, need to be reordered)
            count[h]-=1
        
        return res