class Solution:
    
    def countSubstrings(self, s: str) -> int:
        self.cnt = 0
        n = len(s)
        
        for i in range(n):
            """
            Starting at every index in the string
            We try to count number of odd length and even length palindrome substring. 
            """
            self.solve(s, i, i)
            self.solve(s, i, i+1)
            
        return self.cnt
    
    def solve(self, s, left, right):
        n = len(s)
        
        while 0<=left<=right<len(s) and s[left]==s[right]:
            self.cnt+=1
            left-=1
            right+=1
            
            