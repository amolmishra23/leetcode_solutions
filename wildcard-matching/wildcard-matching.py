class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @functools.lru_cache(None)
        def solve(s, p, i, j):
            # if end of pattern, and also end of string. Pattern match is success.
            if j==len(p): return i==len(s)
            
            # To handle cases like "aa" and "*", where we essentially need code to go solve(s,p,2,1) so it returns true. 
            if i>len(s): return False
            
            if p[j]=="*":
                # on encounter of *, we can either match 0 or n characters.
                # to match 0 chars means we need to match i with j+1. Moved 1 in pattern, but orig string i index is same
                # to match n chars, means we need to match i+1 char with j. Moved 1 in string, but pattern is intact. 
                return solve(s, p, i, j+1) or solve(s, p, i+1, j)
            
            # or the char has to be ? or both chars have to be same to same. 
            return i<len(s) and (p[j]=="?" or p[j]==s[i]) and solve(s, p, i+1, j+1)
        
        return solve(s, p, 0, 0)
            
            