class Solution:
    @functools.lru_cache(None)
    def solve(self, pos, restricted, nonzero, mask):
        """
        We solve this problem using digit dp
        For caching the digits seen so far, we use a mask
        We keep a track of, if number is nonzero or not to decide, if to include in result
        
        limit is based on if restricted, digit at pos in self.s
        
        we change the bitmask only if we encountered a non-zero num. 
        Else dont need numbers like 001. 
        not recommended to change bitmask in number which is not yet started. 
        """
        if pos == len(self.s):
            return 1 if nonzero else 0
        
        limit = 9 if restricted==False else int(self.s[pos])
        res = 0
        
        for i in range(limit+1):
            curr_restricted = restricted
            if i<limit:
                curr_restricted = False
            
            curr_nonzero = nonzero
            if i!=0: curr_nonzero=True
                
            curr_mask = mask
            if curr_nonzero:
                curr_mask |= (1<<i)
                
            if (mask & (1<<i))==0:
                res += self.solve(pos+1, curr_restricted, curr_nonzero, curr_mask)
            
        return res
        
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0: return 1
        self.s = str((10**n)-1)
        return self.solve(0, True, False, 0)+1