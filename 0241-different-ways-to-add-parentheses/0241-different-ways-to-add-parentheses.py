class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = {
            "+": lambda x,y: x+y,
            "-": lambda x,y: x-y,
            "*": lambda x,y: x*y
        }
        
        res = []
        
        for i, char in enumerate(expression):
            if char in ops:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                
                res.extend([ops[char](l, r) for l in left for r in right])
                
        return res if res else [int(expression)]