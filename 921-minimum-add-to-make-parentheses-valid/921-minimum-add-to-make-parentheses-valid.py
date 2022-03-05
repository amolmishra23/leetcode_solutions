class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        if len(S)==0: return 0
        stk, res = [], 0
        
        for x in S:
            if x=="(":
                stk.append(x)
            else:
                if not stk: res+=1
                else: stk.pop()
        
        return res+len(stk)