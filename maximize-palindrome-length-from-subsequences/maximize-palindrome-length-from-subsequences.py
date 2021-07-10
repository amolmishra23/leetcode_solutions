class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        @functools.lru_cache(None)
        def lcs(s, i, j):
            if i>j: return 0
            
            if i==j: return 1+lcs(s, i+1, j-1)
            
            if s[i]==s[j]:
                temp = 2+lcs(s, i+1, j-1)
                if i<self.boundary and j>=self.boundary:
                    self.max_ = max(self.max_,temp)
                return temp
            
            return max(lcs(s, i+1,j), lcs(s, i, j-1))
        
        self.boundary, self.max_ = len(word1), 0
        word = word1+word2
        lcs(word, 0, len(word)-1)
        return self.max_
        
        