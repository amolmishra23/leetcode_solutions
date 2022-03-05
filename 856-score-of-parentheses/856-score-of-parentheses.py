class Solution:
    """
    Main concept to focus is how deep level we go in brackets. 
    1.  Deepest we go, we make the value as 1
        As we keep coming out, we multiply it by 2
    2. The part of where sequential brackets add up. Is taken care by having topmost level imaginary stack. 
    """
    def scoreOfParentheses(self, S: str) -> int:
        stk = [0]
        
        for x in S:
            if x == "(":
                stk.append(0)
            else:
                v = stk.pop()
                stk[-1] += max(2*v, 1)
        
        return stk.pop()