class Solution:
    def checkRecord(self, s: str) -> bool:
        ac, lc = 0, 0
        
        for i in range(len(s)):
            if s[i]=="A":
                ac += 1
                if ac>1: return False
            elif s[i]=="L":
                if i>0 and s[i-1]=="L": lc += 1
                else: lc = 1
                if lc>=3: return False
                
        return True