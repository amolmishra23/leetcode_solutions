class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk, res = [], ""
        for x in s:
            if stk and stk[-1][0]==x: stk[-1][1]+=1
            else: stk.append([x, 1])
            if stk[-1][1] == k: stk.pop()
        for elem, count in stk: res += elem*count        
        return res