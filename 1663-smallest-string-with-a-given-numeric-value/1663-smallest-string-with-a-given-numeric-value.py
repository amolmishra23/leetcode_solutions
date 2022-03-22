class Solution:
    """
    Goal here is, to create "n" length string with sum total as "k"
    a has 1, b has 2, z has 26. In sum.
    So in best case possible if n==k, we can just send "a"*n. 
    If thats not the case, we try to add as many "z" as possible from the end. 
    If z is getting more, we find the mod, and add the character which is mod value. 
    In the end our response is going to be 'a'*(n-z-1) + special_char + 'z'*z
    
    n-z-1 because, we subtract number of z added. And the one special character added. 
    """
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