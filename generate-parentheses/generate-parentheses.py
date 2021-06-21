class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Only condition to be taken care of here is opening should be greater than or equal to closing
        Else we cant simply put a closing bracket
        """
        def solve(op, cl, n, curr, res):
            if op==0 and cl==0:
                # cant proceed any further
                res.append(''.join(curr))
                return
            
            if op>=1:
                curr.append("(")
                solve(op-1, cl, n, curr, res)
                curr.pop()
                
            if op<n and op<cl:
                curr.append(")")
                solve(op, cl-1, n, curr, res)
                curr.pop()
                
        res = []
        solve(n, n, n, [], res)
        return res