class Solution:
    def isHappy(self, n: int) -> bool:
        def square_of_digits(n):
            res = 0
            while n:
                res += (n%10)**2
                n//=10
            return res
        
        visited = set()
        
        while n!=1 and n not in visited:
            visited.add(n)
            n = square_of_digits(n)
            
        return n==1