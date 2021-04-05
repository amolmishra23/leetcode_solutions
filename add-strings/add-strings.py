class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = list(num1), list(num2)
        carry, res = 0, deque()
        
        while num1 or num2:
            n1 = ord(num1.pop())-ord('0') if num1 else 0
            n2 = ord(num2.pop())-ord('0') if num2 else 0
            
            temp = n1+n2+carry
            res.appendleft(temp%10)
            carry = temp//10
            
        if carry: res.appendleft(carry)
        return ''.join(map(str, res))
        