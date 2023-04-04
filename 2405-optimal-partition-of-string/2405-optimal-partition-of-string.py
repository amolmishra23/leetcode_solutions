class Solution:
    def partitionString(self, s: str) -> int:
        map_, cuts = 0, 1
        
        for i,c in enumerate(s):
            ch = ord(c)-ord('a')
            if 1<<ch & map_ != 0: cuts += 1; map_ = 0
            map_ |= (1<<ch)
        
        return cuts