class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MODULO = (10 ** 9) + 7
        res = 1
        l = 1
        for i in range(2, n+1):
            if i & (i-1) == 0: # Check if i is the power of 2
                l += 1
            res = ( (res << l) + i ) % MODULO 
        return res % MODULO