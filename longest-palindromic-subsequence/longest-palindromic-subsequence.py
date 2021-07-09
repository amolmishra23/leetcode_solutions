class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @functools.lru_cache(None)
        def lcs(s1, s2, i, j):
            if i>=len(s1) or j>=len(s2): return 0
            
            if s1[i]==s2[j]: return 1+lcs(s1,s2,i+1,j+1)
            
            return max(lcs(s1,s2,i+1,j), lcs(s1,s2,i,j+1))
        
        return lcs(s, s[::-1], 0, 0)