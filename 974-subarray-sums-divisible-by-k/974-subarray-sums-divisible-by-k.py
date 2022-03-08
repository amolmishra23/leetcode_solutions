class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        preSums = {0: 1}
        s = 0
        res = 0
        for x in A:
            s = (s + x) % K
            res += preSums.get(s, 0)
            preSums[s] = preSums.get(s, 0) + 1
        return res