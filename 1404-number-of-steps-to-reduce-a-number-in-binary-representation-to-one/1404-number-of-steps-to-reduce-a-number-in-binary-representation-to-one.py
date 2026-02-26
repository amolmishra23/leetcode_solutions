class Solution:
    def numSteps(self, s: str) -> int:
        res, n = 0, int(s, 2)
        
        while n:
            if n==1: return res
            if n%2==0: n>>=1
            else: n+=1
            res += 1
        
        return res
            