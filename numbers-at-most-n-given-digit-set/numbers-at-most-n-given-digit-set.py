class Solution:
    @functools.lru_cache(None)
    def solve(self, pos, started, restricted):
        # All that matters is, we shouldnt exceed the S.
        # So checking if we reached the end. 
        if pos == len(self.s):
            return 1 if started==True else 0
        
        res = 0
        # Limit upper end is not 9, but the max digit possible.
        limit = int(self.digits[-1]) if restricted==False else int(self.s[pos])
        
        # In order to get all possible, incl single digit nums
        # We keep one recursion trace to have started as false, and keep skipping positions
        if started==False:
            res += self.solve(pos+1, False, False)
        
        # trying each possible digit possible
        for cur_num in self.digits:
            # checking if the curr digit, breaches the limit imposed by S
            curr = int(cur_num)
            if curr>limit: break
                
            # adding restricted just like other digit dp problems
            curr_restricted = restricted
            if curr<limit:
                curr_restricted = False
            
            # keeping track of the result. 
            res += self.solve(pos+1, True, curr_restricted)
            
        return res
    
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        """
        Allowed digits are there
        Limit is given.
        We need to see how many numbers between 0 to limit can we form using the digits. 
        
        We do it using digit dp. 
        """
        self.digits = digits
        self.s = str(n)
        return self.solve(0, False, True)
        
        