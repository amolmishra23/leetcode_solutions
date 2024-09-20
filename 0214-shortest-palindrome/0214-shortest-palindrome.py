class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def compute_lps(pat):
            n = len(pat)
            res = [0]*n
            
            for i in range(1, n):
                j = res[i-1]
                
                while j>0 and pat[i] != pat[j]:
                    j = res[j-1]
                    
                if pat[i]==pat[j]: j+=1
                    
                res[i] = j
                
            return res
        
        # whatever part prefix==suffix
        # remaining whatever is left, we reverse it and attach at beginning of the string
        lps = compute_lps(s + "#" + s[::-1])
        
        return s[lps[-1]:][::-1] + s