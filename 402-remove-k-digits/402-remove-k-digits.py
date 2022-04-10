class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        
        for n in num:
            if not stk: stk.append(n)
            else:
                while stk and stk[-1]>n and k:
                    stk.pop()
                    k-=1
                stk.append(n)
                
        while k:
            stk.pop()
            k-=1
            
        return "".join(stk).lstrip("0") or "0"