class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        We need to check for all the substrings from beginning to mid of the string
        If repeting it any number of times, can fetch the actual string
        More like abab
        We check a*4==s
        Or ab*2==s. Then we return true
        Beyond half, we dont check because anyways cant get output
        """
        rep, n = "", len(s)
        
        for i in range(n//2):
            rep += s[i]
            if n%(i+1) == 0:
                if rep*(n//(i+1)) == s: return True
                
        return False