class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @functools.lru_cache(None)
        def lcs(s1, s2, i, j):
            if i>=len(s1) or j>=len(s2): return 0
            
            if s1[i]==s2[j]: return 1+lcs(s1, s2, i+1, j+1)
            
            return max(lcs(s1, s2, i+1, j), lcs(s1, s2, i, j+1))
        
        common = lcs(word1, word2, 0, 0)
        
        return len(word1)+len(word2)-2*common