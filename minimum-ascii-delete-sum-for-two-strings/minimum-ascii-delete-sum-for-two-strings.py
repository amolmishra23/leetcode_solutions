class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def cust(s1, s2):
            if len(s1)>len(s2): return 
        
        @functools.lru_cache(None)
        def lcs(s1, s2, i, j):
            if i>=len(s1) or j>=len(s2): return 0
            
            if s1[i]==s2[j]: return ord(s1[i])+lcs(s1, s2, i+1, j+1)
            
            return max(
                lcs(s1, s2, i+1, j), 
                lcs(s1, s2, i, j+1)
            )
            
        return sum(map(ord, s1+s2))-2*lcs(s1,s2,0,0)