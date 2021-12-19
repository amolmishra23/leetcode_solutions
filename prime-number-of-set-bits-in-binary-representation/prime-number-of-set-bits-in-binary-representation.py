class Solution:
    """
    This is a digit dp problem
    """
    @functools.lru_cache(None)
    def solve(self, pos, restricted, s):
        if pos>=len(self.num):
            return 1 if s in self.primes else 0
        
        limit = int(self.num[pos]) if restricted else 1
        res = 0
        
        for i in range(limit+1):
            temp_restrict = restricted
            if i<limit:
                temp_restrict = False
            res += self.solve(pos+1, temp_restrict, s+i)

        return res
        
    
    def countPrimeSetBits(self, left: int, right: int) -> int:
        self.primes = set([2,3,5,7,11,13,17,19])
        
        self.num = str(bin(left-1)[2:])
        a = self.solve(0, True, 0)
        
        self.solve.cache_clear()
        
        self.num = str(bin(right)[2:])
        b = self.solve(0, True, 0)
        
        return b-a