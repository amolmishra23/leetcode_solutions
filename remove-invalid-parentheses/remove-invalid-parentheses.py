class Solution:
    def findRemovals(self, s):
        stk = []
        
        for x in s:
            if x=="(": stk.append("(")
            elif x==")":
                if stk and stk[-1]=="(": stk.pop()
                else: stk.append(")")
                    
        return len(stk)
    
    @functools.lru_cache(None)
    def solve(self, s, removals):
        if removals == 0:
            if self.findRemovals(s) == 0:
                self.res.append(s)
            return
        
        for i in range(len(s)):
            a = s[:i]
            b = s[i+1:]
            self.solve(a+b, removals-1)
            
        
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.res = []
        removals = self.findRemovals(s)
        self.solve(s, removals)
        return self.res