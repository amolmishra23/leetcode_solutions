import operator
class Solution:
    def calculate(self, s: str) -> int:
        def compute(operators, operands):
            right = operands.pop() if operands else 0
            left = operands.pop() if operands else 0
            operands.append(
                ops[operators.pop()](left, right)
            )
            
        ops = {
            "+": operator.iadd,
            "-": operator.isub,
            "*": operator.imul,
            "/": operator.floordiv
        }
        numbers = set(str(x) for x in range(10))
        precedence = {
            "+": 0, "-": 0, "*":1, "/": 1
        }
        
        operands, operators, operand = [], [], 0
        
        for i, token in enumerate(s):
            if token in numbers:
                operand = operand*10 + int(token)
                if i==len(s)-1 or s[i+1] not in numbers:
                    operands.append(operand)
                    operand = 0
            elif token=="(":
                operators.append(s[i])
            elif token==")":
                while operators[-1]!="(":
                    compute(operators, operands)
                operators.pop()
            elif token in precedence:
                while operators and operators[-1] in precedence and precedence[operators[-1]] >= precedence[s[i]]:
                    compute(operators, operands)
                operators.append(token)
        
        while operators:
            compute(operators, operands)
        
        return operands[-1]
            