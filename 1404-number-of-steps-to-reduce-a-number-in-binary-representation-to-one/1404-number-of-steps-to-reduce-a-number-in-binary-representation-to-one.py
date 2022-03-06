class Solution:
    def numSteps(self, s: str) -> int:
        cnt = 1
        num = int(s, 2)
        if num == 1: return 0
        while num:
            if num % 2 == 0:
                num >>= 1
            else:
                num += 1
                
            if num == 1:
                return cnt
            cnt += 1
        
        return cnt