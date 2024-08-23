class Solution:
    def fractionAddition(self, expression: str) -> str:
        def gcd(i, j):
            while j: i, j = j, i%j
            return i
        
        exp = expression.replace("+", " +").replace("-", " -").split()
        A, B = 0, 1
        
        for num in exp:
            a, b = num.split("/")
            a, b = int(a), int(b)
            A = A*b + B*a
            B *= b
            divisor = gcd(A, B)
            A//=divisor
            B//=divisor
            
        return str(A)+"/"+str(B)