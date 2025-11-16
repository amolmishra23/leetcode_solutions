class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9+7
        res, count = 0, 0

        for ch in s:
            if ch=="1":
                count += 1
            else:
                res += (count * (count+1))//2
                count = 0

        res += (count * (count+1))//2

        return res % MOD