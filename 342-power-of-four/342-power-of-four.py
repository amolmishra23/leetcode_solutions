import math 

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and (num & (num - 1)) == 0 and \
               ((num & 0b01010101010101010101010101010101) == num)