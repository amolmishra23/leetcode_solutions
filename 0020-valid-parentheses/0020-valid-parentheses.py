class Solution:
    def isValid(self, s: str) -> bool:
        parens = {
            "(": ")", "{":"}", "[":"]"
        }
        stk = []
        
        if len(s)%2: return False
        
        for ch in s:
            if ch in parens: stk.append(ch)
            elif not (stk and parens[stk.pop()]==ch): return False
        
        return len(stk)==0