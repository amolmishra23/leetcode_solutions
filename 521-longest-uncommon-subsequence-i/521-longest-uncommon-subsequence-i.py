class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        """
        
        Two strings are not of same length, it is clearly the longest one is the answer.
        Then for two strings with same length, if anyone of them has a char which the other string does not have, clearly the whole string's length is the answer.
        Then for two strings with same charset, one string is just a combination of chars of another string, I thought about the ordering of chars matters here. Then I got it, if they are not equal, we can quickly decide, which also covers case 2).
        """
        if a==b: return -1
        
        return max(len(a), len(b))