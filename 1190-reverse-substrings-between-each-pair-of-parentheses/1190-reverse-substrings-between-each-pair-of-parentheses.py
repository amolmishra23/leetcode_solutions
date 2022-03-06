class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = [""]
        
        for x in s:
            if x=="(": stk.append("")
            elif x==")": v = stk.pop(); stk[-1] += v[::-1]
            else: stk[-1] += x
        
        return stk[-1]