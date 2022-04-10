class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solve(op, cl, n):
            if op==0 and cl==0:
                res.append("".join(curr))
                return 
            
            if op >= 1:
                curr.append("(")
                solve(op-1, cl, n)
                curr.pop()
                
            if op<cl and cl>=1:
                curr.append(")")
                solve(op, cl-1, n)
                curr.pop()
        
        res, curr = [], []
        solve(n, n, n)
        return res