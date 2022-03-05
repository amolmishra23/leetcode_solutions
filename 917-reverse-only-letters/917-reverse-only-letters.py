class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        start, end = 0, len(s)-1
        txt = list(s)
        
        while start<end:
            if not txt[start].isalpha(): start+=1
            elif not txt[end].isalpha(): end-=1
            else: txt[start], txt[end] = txt[end], txt[start]; start+=1; end-=1
            
        return ''.join(txt)
            