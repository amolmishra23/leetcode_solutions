class Solution:
    def longestPalindrome(self, s: str) -> str:
        @functools.lru_cache(None)
        def solve(s, i, j):
            if i>j: return ""
            if i==j: return s[i]

            if s[i]==s[j]:
                rem = solve(s, i+1, j-1)
                if len(rem)==(j-1)-(i+1)+1: return s[i:j+1]

            left = solve(s, i+1, j)
            right = solve(s, i, j-1)

            return max(left, right, key=len)

        return solve(s, 0, len(s)-1)
