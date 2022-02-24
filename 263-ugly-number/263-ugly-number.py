class Solution:
    def isUgly(self, n: int) -> bool:
        """
        Goal is to check if n is divisible by only 2/3/5
        We can go in waterfall model. 
        """
        # not perfectly divided, hence not ugly number
        if n==0: return False
        # perfectly divided one of the previous numbers by 2/3/5
        elif n==1: return True
        elif n%2==0: return self.isUgly(n//2)
        elif n%3==0: return self.isUgly(n//3)
        elif n%5==0: return self.isUgly(n//5)
        
        # not divisible by any of 2/3/5. Hence return False
        return False