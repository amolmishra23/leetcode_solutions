class Solution:
    def minSwaps(self, s: str) -> int:
        stk, mismatch = [], 0
        
        for ch in s:
            if ch=="[":
                stk.append(ch)
            else:
                if stk: stk.pop()
                else: mismatch+=1
                    
        return (mismatch+1)//2
            