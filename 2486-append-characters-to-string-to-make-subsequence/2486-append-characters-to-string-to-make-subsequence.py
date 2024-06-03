class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        @lru_cache(None)
        def lcs(i, j):
            if i>=len(s) or j>=len(t): return 0
            
            if s[i]==t[j]: return 1+lcs(i+1, j+1)
            
            return max(lcs(i+1, j), lcs(i, j+1))
        
        i, j = 0, 0
        while i<len(s) and j<len(t):
            if s[i]==t[j]: i+=1; j+=1
            else: i+=1
        
        return len(t)-j