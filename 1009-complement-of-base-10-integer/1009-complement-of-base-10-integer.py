class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if not n: return 1
        mask = 0
        temp = n
        while temp:
            mask = (mask << 1) | 1
            temp >>= 1
        return n ^ mask