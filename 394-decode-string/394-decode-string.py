class Solution:
    def decodeString(self, s: str) -> str:
        stk = [["", 1]]
        num = ""
        
        for x in s:
            if x.isdigit():
                num += x
            elif x=="[":
                stk.append(["", int(num)])
                num = ""
            elif x=="]":
                ch, count = stk.pop()
                stk[-1][0] += ch*count
            else:
                stk[-1][0] += x
        
        return stk[-1][0]