class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def solve(s):
            stk = []
            for x in s:
                if x=="#":
                    if stk: stk.pop()
                else:
                    stk.append(x)

            return "".join(stk)
        
        a, b = solve(S), solve(T)
        return a==b
            
            