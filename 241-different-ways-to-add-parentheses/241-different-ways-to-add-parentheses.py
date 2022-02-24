class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = {
            "+": lambda x, y : x + y,
            "-": lambda x, y : x - y,
            "*": lambda x, y : x * y
        }
        res = []
        for x, char in enumerate(expression):
            if char in ops:
                leftResults = self.diffWaysToCompute(expression[:x])
                rightResults = self.diffWaysToCompute(expression[x + 1:])
                
                for leftNum in leftResults:
                    for rightNum in rightResults:
                        res.append(ops[char](leftNum, rightNum))
        
        # no operations means expression is a sole number
        if not res:
            res.append(int(expression))
        return res