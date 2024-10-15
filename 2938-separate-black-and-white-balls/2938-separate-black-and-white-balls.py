class Solution:
    def minimumSteps(self, s: str) -> int:
        l, res = 0,0
        
        for r in range(len(s)):
            if s[r]=="0":
                res += (r-l)
                l+=1
                
        return res
    
    def minimumSteps1(self, s: str) -> int:
        s = list(s)
        l, r, res = 0, 0, 0
        
        while r<len(s):
            if s[r]=="1": r+=1; continue
            
            s[l], s[r] = s[r], s[l]
            res += (r-l)
            r+=1; l+=1
            
        return res