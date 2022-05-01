class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def solve(s):
            stk = []
            for x in s:
                if x=="#":
                    if stk: stk.pop()
                else: stk.append(x)

            return "".join(stk)
        
        return solve(S) == solve(T)
            
            