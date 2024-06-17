class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c<0: return False
        
        a, b = 0, int(math.sqrt(c))
        
        while a<=b:
            temp = a**2 + b**2
            
            if temp==c: return True
            elif temp>c: b-=1
            else: a+=1
        
        return False