class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        @lru_cache(None)
        def dp(i, j):
            if j==n: return i==m
            
            if j+1<n and p[j+1]=="*":
                res = dp(i, j+2)
                if not res:
                    if i<m and (s[i]==p[j] or p[j]=="."):
                        res = dp(i+1, j)
                return res
            
            if i<m and (s[i]==p[j] or p[j]=="."): return dp(i+1, j+1)
            
            return False
        
        return dp(0, 0)
            