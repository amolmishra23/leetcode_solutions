class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        vals = path.split("/")
        
        for val in vals:
            if val==".." and stk: stk.pop()
            elif val not in [".", "..", ""]: stk.append(val)
        
        return "/" + "/".join(stk)