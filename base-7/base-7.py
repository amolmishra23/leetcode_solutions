class Solution:
    def convertToBase7(self, num: int) -> str:
        """
        Easy way to think of it is, how do we convert number to binary??
        We keep finding mod 2, and and inturn keep dividing the number by 2
        """
        if num==0: return "0"
        
        res, n = [], abs(num)
        
        while n:
            res.append(str(n%7))
            n //= 7
            
        res_str = ''.join(res[::-1])
        
        return '-'+res_str if num<0 else res_str