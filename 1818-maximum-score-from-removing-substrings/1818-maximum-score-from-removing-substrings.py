class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        for q,t in sorted(((x, "ab"), (y, "ba")))[::-1]:
            stk = []
            for ch in s:
                if stk and stk[-1]+ch == t:
                    res += q
                    stk.pop()
                else:
                    stk.append(ch)

            s = stk

        return res