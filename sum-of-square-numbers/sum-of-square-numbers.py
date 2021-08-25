class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c<0: return false
        
        # for sure the boundary has to be less than b. 
        a, b = 0, int(math.sqrt(c))
        
        # its also allowed to have a,b as same. Hence a<=b
        while a<=b:
            temp = a**2 + b**2
            if temp==c:
                return True
            elif temp>c:
                b-=1
            else:
                a+=1
        
        return False