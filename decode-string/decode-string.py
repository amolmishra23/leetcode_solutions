class Solution:
    def decodeString(self, s: str) -> str:
        """
        This question can very well be solved using a stack
        """
        stk = [
            ["", 1]
        ]
        num = ""
        
        for a in s:
            if a.isdigit(): num+=a
            elif a=="[":
                stk.append(["", int(num)])
                num = ""
            elif a=="]":
                txt, count = stk.pop()
                stk[-1][0] += txt*count
            else:
                stk[-1][0] += a
        
        return stk[-1][0]
                