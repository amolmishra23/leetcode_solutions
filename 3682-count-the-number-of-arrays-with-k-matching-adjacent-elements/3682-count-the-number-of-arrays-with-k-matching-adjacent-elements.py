class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        if k > n - 1:
            return 0

        if n == 1:
            return m % MOD
        if n == 2:
            return m % MOD if k == 1 else (m * (m - 1)) % MOD


        prefix = m * pow(m - 1, n - k - 1, MOD) % MOD

        ways_to_place_duplicates = comb(n - 1, k)

        return prefix * ways_to_place_duplicates % MOD