class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Classic problem to solve using bitwise operators.
        Explanation is there in here: https://www.youtube.com/watch?v=m4L_5qG4vG8
        """
        if dividend == 1<<31 and divisor==-1: return 2<<30-1
        
        sign = len(set([dividend>=0, divisor>=0]))==1
        
        dvd, dvs = abs(dividend), abs(divisor)
        res = 0
        
        while dvd-dvs >= 0:
            count = 0
            
            while dvd - (dvs<<1<<count) >= 0:
                count += 1
            
            res += 1<<count
            dvd -= dvs<<count
            
        return min(max(-(2<<30), res if sign else -res), (2<<30)-1)
        