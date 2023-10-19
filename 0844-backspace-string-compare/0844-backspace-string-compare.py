class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def solve(s):
            stk = []
            for ch in s:
                if ch=="#":
                    if stk: stk.pop()
                else: stk.append(ch)
                    
            return "".join(stk)
        
        return solve(S)==solve(T)