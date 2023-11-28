class Solution:
    def numberOfWays(self, corridor: str) -> int:
        chCount, res = 0, 1
        lastIdx = -1
        MOD = (10**9)+7
        
        for i, ch in enumerate(corridor):
            if ch=="P": continue
            chCount += 1
            if chCount>=3 and chCount%2==1:
                res = (res * (i-lastIdx))%MOD
            lastIdx = i
                
        return 0 if chCount==0 or chCount%2==1 else res