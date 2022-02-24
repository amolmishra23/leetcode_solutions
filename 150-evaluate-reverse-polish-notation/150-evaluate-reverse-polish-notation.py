
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        ops = ['+','-','*', '/']
        for token in tokens:
            if token in ops:
                n2 = res.pop() # Pop out in reverse order
                n1 = res.pop()
                res.append(int(eval(str(n1) + token + str(n2)))) # evaluate statement
            else:
                res.append(token) # keep on appending numbers
        return res[0]