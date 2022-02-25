class Solution:
    def decodeString(self, s: str) -> str:
        """
        Lets solve it using a stack.
        We have 4 kinds of chars: num, char, [, ]
        On each type of them, we do different kind of operation
        """
        stk = [["", 1]]
        num = ""
        
        for x in s:
            if x.isdigit():
                num += x
            elif x=="[":
                stk.append(["", int(num)])
                num = ""
            elif x=="]":
                char, count = stk.pop()
                stk[-1][0] += char*count
            else:
                stk[-1][0] += x
                
        return stk[-1][0]
                