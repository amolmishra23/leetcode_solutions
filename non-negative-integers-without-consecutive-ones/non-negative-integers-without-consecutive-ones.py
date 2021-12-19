class Solution:
    @functools.lru_cache(None)
    def solve(self, pos, restricted, prev):
        if pos >= len(self.num):
            return 1
        
        limit = int(self.num[pos]) if restricted else 1
        res = 0
        
        for i in range(limit+1):
            temp_restrict = restricted
            if i<limit:
                temp_restrict=False
            if prev!=1 or i!=1:
                res += self.solve(pos+1, temp_restrict, i)
                
        return res
        
    def findIntegers(self, n: int) -> int:
        self.num = str(bin(n)[2:])
        return self.solve(0, True, 0)
        