class Solution:
     def breakPalindrome(self, S):
        # this is a pretty easy question
        # find the first non 'a' to be replaced as 'a' character
        for i in range(len(S) // 2):
            if S[i] != 'a':
                return S[:i] + 'a' + S[i + 1:]
        
        # if we reached this step, means entire string is full of 'a' chars only
        # so, we basically change the last char to 'b'
        return S[:-1] + 'b' if S[:-1] else ''