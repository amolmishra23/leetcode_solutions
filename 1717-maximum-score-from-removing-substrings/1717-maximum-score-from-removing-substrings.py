class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:            
        def solve(pair, score):
            nonlocal s
            res, stk = 0, []
            for ch in s:
                if ch==pair[1] and stk and stk[-1]==pair[0]: 
                    stk.pop(); res+=score
                else:
                    stk.append(ch)
            
            s = "".join(stk)
            return res
        
        mx = "ab" if x>y else "ba"
        return solve(mx, max(x, y)) + solve(mx[::-1], min(x,y))