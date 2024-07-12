class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def solve(s, ch1, ch2):
            res, stk = 0, []
            for ch in s:
                if ch==ch2 and stk and stk[-1]==ch1: 
                    stk.pop(); res+=x
                else:
                    stk.append(ch)
            
            s = "".join(stk)
            stk = []
            for ch in s:
                if ch==ch1 and stk and stk[-1]==ch2:
                    stk.pop(); res+=y
                else:
                    stk.append(ch)
            
            return res
        
        mx = "ab" if x>y else "ba"
        if y>x: x,y=y,x
        return solve(s, mx[0], mx[1])