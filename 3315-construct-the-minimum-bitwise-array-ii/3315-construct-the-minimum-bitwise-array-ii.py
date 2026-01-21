from typing import List

class Solution:
    def minBitwiseArray(self, values: List[int]) -> List[int]:
        res = []

        for cur in values:
            if cur == 2:
                res.append(-1)
                continue

            temp = cur
            cnt = 0

            while temp & 1:
                cnt += 1
                temp >>= 1

            res.append(cur - (1 << (cnt - 1)))

        return res