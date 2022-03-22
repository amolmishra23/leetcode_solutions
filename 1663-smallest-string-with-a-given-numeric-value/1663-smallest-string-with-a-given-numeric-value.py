class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        # assume every char is an 'a' total = new k
        total = k - n
        
        # counts how many z are needed
        z = total//25
        
        # checks if any non 'a' or non 'z' is needed
        if total % 25 == 0: return 'a'*(n-z) + 'z'*z
        
        # get non 'a' or non 'z'
        special_char = string.ascii_lowercase[total%25]
        
        # return the string
        return 'a'*(n-z-1) + special_char + 'z'*z