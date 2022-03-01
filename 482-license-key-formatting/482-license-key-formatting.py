class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        if len(s)-s.count("-")==0: return ""
        res, cnt = [], 0
        
        for c in s[::-1]:
            if c!="-":
                res.append(c.upper())
                cnt +=1
            if cnt==k:
                res.append("-")
                cnt=0
                
        if res[-1]=="-": res.pop()
        
        return "".join(res[::-1])
        
        