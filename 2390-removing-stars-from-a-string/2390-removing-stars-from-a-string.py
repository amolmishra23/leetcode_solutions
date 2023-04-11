class Solution:
    def removeStars(self, s: str) -> str:
        j, s = 0, list(s)
        
        for i in range(len(s)):
            if s[i]=="*": j-=1
            else: s[j]=s[i]; j+=1
        
        return "".join(s[:j])