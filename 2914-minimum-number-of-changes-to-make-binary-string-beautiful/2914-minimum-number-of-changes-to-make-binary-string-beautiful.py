class Solution:
    def minChanges(self, s: str) -> int:
        count, i = 0, 0
        
        while i<len(s)-1:
            if s[i]!=s[i+1]:
                count += 1
            i+=2
            
        return count