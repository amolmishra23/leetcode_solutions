class Solution:
    def makeFancyString(self, s: str) -> str:
        s, res = list(s), list()
        for i in range(len(s)):
            if i>=2 and s[i]==s[i-1]==s[i-2]:
                continue
            else:
                res.append(s[i])
        
        return "".join(res)