class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cnt, res = 0, 0
        for ch in s:
            if ch=="(":
                cnt +=1
            else:
                if cnt: cnt-=1
                else: res+=1
        
        res+=cnt
        return res