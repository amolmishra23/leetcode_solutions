class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        def add2(x,y):
            while (y != 0):
                c=x&y
                x=x^y
                y=c<<1
            return x
        
        def minus2(x,y):
            while (y != 0): 
                borrow = (~x) & y 
                x = x ^ y 
                y = borrow << 1
            return x 
        
        if a == 0:
            return b
        if b == 0:
            return a
        
        if a > 0 and b > 0:
            return add2(a,b)
        elif a < 0 and b < 0:
            return -add2(abs(a),abs(b))
        elif a < 0 and b > 0:
            if abs(a) >= b:
                return -minus2(abs(a),b)
            if b > abs(a):
                return minus2(b,abs(a))
        elif b < 0 and a > 0:
            if abs(b) >= a:
                return -minus2(abs(b),a)
            if a > abs(b):
                return minus2(a,abs(b))