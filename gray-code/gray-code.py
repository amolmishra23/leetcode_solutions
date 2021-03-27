class Solution:
    def grayCode(self, n: int) -> List[int]:
        def solve(n):
            if n==0: return ["0"]
            if n==1: return ["0", "1"]
            res = solve(n-1)
            return ["0"+s for s in res]+["1"+s for s in res[::-1]]
        return [int(s, 2) for s in solve(n)]