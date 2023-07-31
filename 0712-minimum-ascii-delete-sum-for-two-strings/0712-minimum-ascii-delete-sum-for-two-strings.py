class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @lru_cache(None)
        def lcs(i, j):
            if i>=len(s1) or j>=len(s2): return 0
            
            if s1[i]==s2[j]: return ord(s1[i]) + lcs(i+1, j+1)
            
            return max(lcs(i, j+1), lcs(i+1, j))
        
        return sum(map(ord, s1+s2)) - 2*lcs(0, 0)