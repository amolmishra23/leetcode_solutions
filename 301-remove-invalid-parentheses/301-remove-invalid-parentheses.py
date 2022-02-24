class Solution:
    def findRemovals(self, s):
        """
        Number of removals is, number of extra parenthesis we have in the end after rebalancing. 
        """
        stk = []
        
        for x in s:
            if x=="(": stk.append("(")
            elif x==")":
                if stk and stk[-1]=="(": stk.pop()
                else: stk.append(")")
                    
        return len(stk)
    
    @functools.lru_cache(None)
    def solve(self, s, removals):
        """
        If we cannot make any further removals, and we have a balanced string, we add it to our result.
        """
        if removals == 0:
            if self.findRemovals(s) == 0:
                self.res.append(s)
            return
        
        """
        Else we remove 1 parenthesis each at each char possible. And then recursively check if it was good enough.
        """
        for i in range(len(s)):
            a = s[:i]
            b = s[i+1:]
            self.solve(a+b, removals-1)
            
        
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # find min number of removals required
        self.res = []
        removals = self.findRemovals(s)
        # populate all the valid strings after the removal. 
        self.solve(s, removals)
        return self.res