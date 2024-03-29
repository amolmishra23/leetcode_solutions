class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(s1, s2, i, j):
          if cache[i][j]!=-1: return cache[i][j]
          if i>=len(s1) or j>=len(s2): return 0

          if s1[i]==s2[j]: cache[i][j] = 1+lcs(s1, s2, i+1, j+1)
          else: cache[i][j] = max(lcs(s1, s2, i+1, j), lcs(s1, s2, i, j+1))

          return cache[i][j]

        cache = [[-1]*(len(text2)+1) for _ in range((len(text1))+1)]
        return lcs(text1, text2, 0, 0)