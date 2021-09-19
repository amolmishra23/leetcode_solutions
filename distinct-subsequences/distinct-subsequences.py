class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @functools.lru_cache(None)
        def solve(i, j):
            # if we have reached end of 2nd string, means its a valid subsequence. Hence return 1
            if j<0: return 1
            
            # if we reached end of 1st string, means its invalid. Hence return 0
            if i<0: return 0
            
            # in case it matched, its valid subsequence candidate
            # but we also want to keep alive possibility of without this character
            if s[i]==t[j]: return solve(i-1, j)+solve(i-1,j-1)
            
            # Applying just the case2 in here. 
            return solve(i-1,j)
        
        return solve(len(s)-1, len(t)-1)