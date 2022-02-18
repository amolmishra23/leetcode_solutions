class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # the trick to build smallest number
        # We need to have a strictly increasing array
        # anywhere we see a dip, we can remove that element. from left=>right
        
        stk = []
        i = 0
        
        for i in range(len(num)):
            if not stk: stk.append(num[i])
            else:
                while stk and stk[-1]>num[i] and k>0:
                    stk.pop()
                    k-=1
                stk.append(num[i])
                
        while stk and k!=0:
            stk.pop()
            k-=1
        
        return "".join(stk).lstrip("0") or "0"