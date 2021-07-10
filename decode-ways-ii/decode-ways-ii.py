class Solution:
    def numDecodings(self, s: str) -> int:
        @functools.lru_cache(None)
        def solve(s, i):
            if i>=len(s): return 1
            
            res, c1 = 0, s[i]
            
            if c1=="*": res += 9*solve(s, i+1)
            elif int(c1)>0: res += solve(s, i+1)
                
            if i+1<len(s):
                c2 = s[i+1]
                if c1=="2" and c2=="*": res += 6*solve(s, i+2)
                elif c1=="1" and c2=="*": res += 9*solve(s, i+2)
                elif c1=="*" and c2=="*": res += 15*solve(s, i+2)
                elif c1=="*" and int(c2)<=6: res+=2*solve(s, i+2)
                elif c1=="*": res+=solve(s, i+2)
                elif int(c1)==1: res+=solve(s, i+2)
                elif int(c1)==2 and int(c2)<=6: res+=solve(s, i+2)
                
            return res%self.const
        
        self.const = (10**9)+7
        return solve(s, 0)