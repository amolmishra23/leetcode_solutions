class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k==1: 
            res = s
            for _ in range(len(s)-1):
                s = s[1:]+s[0]
                res = min(res, s)
            return res
        else:
            return ''.join(sorted(s))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            