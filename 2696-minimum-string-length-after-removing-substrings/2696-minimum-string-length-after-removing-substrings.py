class Solution:
    def minLength(self, s: str) -> int:
        stk = []
        
        for ch in s:
            stk.append(ch)
            if len(stk)>=2 and (stk[-2:]==["A","B"] or stk[-2:]==["C", "D"]):
                stk.pop(); stk.pop()
            
        return len(stk)