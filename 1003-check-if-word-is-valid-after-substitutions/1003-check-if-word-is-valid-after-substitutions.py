class Solution:
    """
    Logic is that, before every c, we should have seen a,b before.
    Keep storing all the a, b character sequences in a stack. 
    And keep popping both of it, whenever we see a character "C"
    """
    def isValid(self, s: str) -> bool:
        stk = []
        
        for i in s:
            if i == 'c':
                if stk[-2:] == ['a', 'b']:
                    stk.pop()
                    stk.pop()
                else:
                    return False
            else:
                stk.append(i)
        
        return not stk