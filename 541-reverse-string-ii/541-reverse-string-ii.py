class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        We iterate in 2k length window. 
        After reversing k chars, we skip the next k chars and keep repeating the process. 
        """
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return ''.join(s)