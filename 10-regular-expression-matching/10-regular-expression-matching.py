class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def dp(i, j):
            if j == len(p):  # If `j` reach end of pattern `p`
                return i == len(s)  # Then it fully matches if and only if `i` reach end of string `s`
				
            if j+1 < len(p) and p[j+1] == '*':
                ans = dp(i, j+2) # match zero chars
                if i < len(s) and (s[i] == p[j] or p[j] == '.'):
                    ans = ans or dp(i+1, j) # match 1 char, skip 1 char in s, don't skip in p since it can march zero or match more characters
                return ans
            if i < len(s) and (s[i] == p[j] or p[j] == '.'):
                return dp(i+1, j+1) # match 1 char, skip 1 char in both s and p
            return False
        
        return dp(0, 0)