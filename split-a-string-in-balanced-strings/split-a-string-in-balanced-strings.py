class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r, l = 0, 0
        res = 0
        
        for ch in s:
            if ch=="R": r+=1
            else: l+=1
            
            if r>=1 and r==l:
                r, l = 0, 0
                res += 1
            
        return res