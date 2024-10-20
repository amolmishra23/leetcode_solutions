class Solution:
    def parseBoolExpr(self, s: str) -> bool:
        stk = []
        
        for c in s:
            if c!=")" and c!=",":
                stk.append(c)
            elif c==")":
                exp = []
                
                while stk and stk[-1]!="(":
                    exp.append(stk.pop() == "t")
                    
                stk.pop()
                
                if stk:
                    t = stk.pop()
                    res = None
                    
                    if t == "&":
                        res = all(exp)
                    elif t == "|":
                        res = any(exp)
                    else:
                        res = not exp[0]
                        
                    stk.append("t" if res else "f")
                    
        return stk[-1] == "t"
                    