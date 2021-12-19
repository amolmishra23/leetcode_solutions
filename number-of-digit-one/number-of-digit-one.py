class Solution:
    @functools.lru_cache(None)
    def solve(self, pos, restricted, s):
        # we have explored all positions in the number
        if pos >= len(self.num):
            return s
        
        # whats our current limit? 
        # assuming we are going for 5624. We do in 2 steps
        # 0-4999 without any limit
        
        # then we start from 5000-5624
        # in this also do first from 5000-5599
        # Then we can see for 624
        # this is how digit dp works
        
        # if we are restricted, We can only iterate until 5, not 9
        # first step we are anyways restricted. 
        limit = int(self.num[pos]) if restricted else 9
        res = 0
        
        
        for i in range(limit+1):
            temp_restrict = restricted 
            if i<limit: 
                temp_restrict = False
            if i==1:
                res += self.solve(pos+1, temp_restrict, s+1)
            else:
                res += self.solve(pos+1, temp_restrict, s)
            
        return res

    def countDigitOne(self, n: int) -> int:
        self.num = str(n)
        return self.solve(0, True, 0)