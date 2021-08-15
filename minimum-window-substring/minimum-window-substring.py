class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # first we find count of all chars in t.
        # the main goal is, if at all all chars in t, count becomes 0, then thats a valid answer. 
        # to count same, we keep matched variable, and compare against len(count_t)
        
        # then we need to find smallest such string. hence we keep shrinking from beginning.
        # in the end we return that particular substring. 
        count = Counter(t)
        ws, rs = 0, 0
        matched = 0
        res = float('inf')
        
        for we in range(len(s)):
            curr = s[we]
            
            if curr in count:
                count[curr]-=1
                if count[curr]==0: matched+=1
                    
            while matched==len(count):
                if (we-ws+1)<res:
                    res = we-ws+1
                    rs = ws
                first = s[ws]
                ws += 1
                if first in count: 
                    if count[first]==0:
                        matched-=1
                    count[first]+=1
            
        return s[rs: rs+res] if res!=float('inf') else ""