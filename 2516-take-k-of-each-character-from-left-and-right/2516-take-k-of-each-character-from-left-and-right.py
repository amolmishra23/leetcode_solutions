class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        """
        making the problem reverse
        instead of solving it for making it minimum length
        lets maximize the middle area of string such that it has expected_count-k for each character
        """
        limits = {c: s.count(c)-k for c in "abc"}
        if any(x<0 for x in limits.values()): return -1
        
        count = {c:0 for c in "abc"}
        res = l = 0
        
        for r in range(len(s)):
            count[s[r]] += 1
            while count[s[r]] > limits[s[r]]:
                count[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
            
        return len(s) - res
        
        