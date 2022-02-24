import operator

class Solution:
    def calculate(self, s: str) -> int:
        def compute(operators, operands):
            b, a = operands.pop(), operands.pop()
            operands.append(
                ops[operators.pop()](a,b)
            )
            
        ops = {
            "+": operator.iadd,
            "-": operator.isub,
            "*": operator.imul,
            "/": operator.floordiv
        }
        
        operators, operands, num = [], [], 0
        numbers = set(str(x) for x in range(10))
        precedence = {
            "+": 0, "-":0, "*":1, "/":1
        }
        
        """
        2*3+5
        We are supposed to 6+5=11
        So after seeing +, we need to mul 2*3, as * has higher precedence. 
        """
        for i,char in enumerate(s):
            if char in numbers:
                num = num*10
                num += int(char)
                if i==len(s)-1 or s[i+1] not in numbers:
                    operands.append(num)
                    num = 0
            elif char == "(":
                operators.append(char)
            elif char == ")":
                while operators[-1]!="(":
                    compute(operators, operands)
                operators.pop()
            elif char in precedence:
                while operators and operators[-1] in precedence and precedence[operators[-1]] >= precedence[char]:
                    compute(operators, operands)
                operators.append(char)
                
        while operators:
            compute(operators, operands)
            
        return operands[-1]