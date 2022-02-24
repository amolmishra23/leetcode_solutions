class Solution:
    @functools.lru_cache(None)
    def solve(self, idx, r, s):
        if idx>=len(self.num):
            return s
        
        lim = int(self.num[idx]) if r==True else 9
        res = 0 
        
        for i in range(lim+1):
            new_r = r
            if i<int(self.num[idx]):
                new_r = False
            if i==1:
                res += self.solve(idx+1, new_r, s+1)
            else:
                res += self.solve(idx+1, new_r, s)
                
        return res
            
    def countDigitOne(self, n: int) -> int:
        self.num = str(n)
        return self.solve(0, True, 0)