class Solution:
    def countBits(self, n: int) -> List[int]:
        # The logic is, for every num, we just check what its curr digit is. 1 or not. 
        # then we right shift it, and use the cached answer. 
        
        # Example if for 100, we will check 100&1. This actually comes to be 0
        # Like this we need to be doing for 10, 1 as well. In the end output is 1. 
        ans = [0]*(n+1)
        
        for i in range(1, n+1):
            ans[i] = ans[i>>1]+(i&1)
            
        return ans