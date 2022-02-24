# class Solution:
#     def reverseBits(self, n: int) -> int:
#         res = 0
#         for _ in range(32):
#             res = (res<<1) + (n&1)
#             n>>=1
#         return res

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for i in range(32):
            result <<= 1
            result |= n&1
            n >>= 1
            
        return result
        