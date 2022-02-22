class Solution:
    def isValid(self, s: str) -> bool:
        parens, stk = {
            '(': ')',
            '{': '}',
            '[': ']'
        }, []
        
        if len(s)%2: return False
        
        for chr in s:
            if chr in parens: stk.append(chr)
            elif not (stk and parens[stk.pop()]==chr): return False
        
        return len(stk)==0