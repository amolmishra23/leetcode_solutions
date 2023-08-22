class Solution:
    def convertToTitle(self, n: int) -> str:
        """
        Actually the n is derived from the string by doing
        n = (A+1) * 26^2 + (B+1) * 26^1 + (Z+1) * 26^0
        We need to find back the string now. 
        We in every step perform the below step:
        n = (A+1) * 26^2 + (B+1) * 26^1 + (Z+1) * 26^0
        
        
        n-1 = (A+1) * 26^2 + (B+1) * 26^1 + Z
        (n-1)%26 =  Z                                                  (1)
        (n-1)/26 = (A+1) * 26^1 + (B+1) * 26^0                         (2)
        """
        res = []
        while n:
            # doing minus 1, because during the computation plus 1 was done, to match 1 indexing
            n-=1
            # just extracting the Z part
            curr_char = n%26
            # for the remaining string
            n //= 26
            res.append(string.ascii_uppercase[curr_char])
            
        return "".join(res[::-1])