class Solution:
    def helper(self, s, i, j):
        while i>=0 and j<len(s) and s[i]==s[j]: 
            i-=1; j+=1
        return s[i+1: j]
    
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            odd_str = self.helper(s, i, i)
            if len(odd_str)>len(res):
                res=odd_str
            
            even_str = self.helper(s, i, i+1)
            if len(even_str)>len(res):
                res=even_str
            
        return res