class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        i = 0
        
        for j in range(0, len(t)):
            if s[i] == t[j]: i+=1
            if i==len(s): break
            
        return i == len(s)