class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # concept from https://www.youtube.com/watch?v=lhhqbGH7Pao
        def compute_lps(pattern):
            n = len(pattern)
            pi = [0]*n
            
            for i in range(1, n):
                j = pi[i-1]
                while j and s[i]!=s[j]:
                    j = pi[j-1]
                
                if s[i]==s[j]: j+=1
                pi[i] = j
                
            return pi
        
        lps = compute_lps(s)
        if lps[-1]==0: return False
        temp = len(s)-lps[-1]
        return len(s)%temp==0 and s[:temp]*(len(s)//temp)==s
            
            