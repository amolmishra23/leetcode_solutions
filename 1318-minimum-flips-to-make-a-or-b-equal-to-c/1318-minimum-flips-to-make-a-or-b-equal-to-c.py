class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        result = 0
        for i in range(31):
            a_i, b_i, c_i = map(lambda x: x&1, [a, b, c])
            if a_i | b_i != c_i:
                # if both a,b are 1, then we need 2 flips
                # else we can just make 1 change to make it equal to c_i
                result += 2 if a_i == b_i == 1 else 1
            # kicking out the last bit.
            a, b, c = a>>1, b>>1, c>>1
        return result