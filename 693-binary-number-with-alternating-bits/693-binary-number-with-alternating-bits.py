class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last_bit = n&1
        expected_bit = 1^last_bit
        n >>= 1
        while n:
            if n&1 != expected_bit:
                return False
            expected_bit ^= 1
            n >>= 1
        return True