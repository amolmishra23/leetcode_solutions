class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ip = [abs(ord(a)-ord(b)) for a,b in zip(s, t)]
        lo, cost, res = 0, 0, 0
        
        for hi in range(len(s)):
            cost += ip[hi]
            
            while cost>maxCost:
                cost -= ip[lo]
                lo += 1
            
            res = max(res, hi-lo+1)
        
        return res 