class Solution:
    def minSwaps(self, s: str) -> int:
        stk, mismatch = 0, 0
        
        for ch in s:
            if ch=="[":
                stk+=1
            else:
                if stk>0: stk-=1
                else: mismatch+=1
                    
        return (mismatch+1)//2
            