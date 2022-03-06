
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res, depth = "", 0
        
        for x in S:
            if x=="(":
                if depth>0: res+=x
                depth += 1
            else:
                depth -= 1
                if depth>0: res+=x
        
        return res