class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        Logic being, just keep count of which is the current string repeating. 
        as soon as we find something different, we count how many 1s and 2s min have occured and add that off to result
        same logic of shirt-pant pairing applies, we have as many pairs as min of them avlb
        """
        if len(s)==1: return 0

        prev, curr, res = 0, 1, 0
        
        for i in range(1, len(s)):
            if s[i]==s[i-1]: curr+=1
            else:
                res+=min(prev, curr)
                prev = curr
                curr = 1

        res += min(prev, curr)
        return res