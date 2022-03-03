class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        dp = [[0]*n for _ in range(n)]
        max_len = 1
        start = 0
        
        # because all the 1 length substrings are actually palindromes
        for i in range(n):
            dp[i][i] = True
            
        # checking for all the 2 length substrings
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1] = True
                start = i
                max_len=2
        
        # checking for all 3..n length possible substrings. 
        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i+k-1
                
                if dp[i+1][j-1] and s[i]==s[j]:
                    dp[i][j] = True
                    
                    if k>max_len:
                        start = i
                        max_len = k
                        
        return s[start:start+max_len]