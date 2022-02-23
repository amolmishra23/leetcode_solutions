class Solution:
    def numDecodings(self, s: str) -> int:
        @functools.lru_cache(None)
        def solve(s, i):
            # if we reached till end of the string, surely its a valid permutation
            # and return 1 so that, it adds up as a valid permutation
            if i>=len(s): return 1
            
            # checking from the current char, and getting all possible valid permutations
            res, c = 0, s[i]
            
            # if char is bigger than 0, chance of a valid permutation
            if int(c)>0: res += solve(s, i+1)
                
            # if char is between 10-26, another chance of a permutation
            if i+1<len(s) and 10<=int(s[i:i+2])<=26: res += solve(s, i+2)
                
            return res
        
        return solve(s, 0)