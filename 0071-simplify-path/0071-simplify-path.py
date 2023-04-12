class Solution:
    def simplifyPath(self, path: str) -> str:
        stk, path = [], path.split("/")
        
        for val in path:
            if val==".." and stk: stk.pop()
            elif val not in {".", "..", ""}: stk.append(val)
                
        return "/" + "/".join(stk)