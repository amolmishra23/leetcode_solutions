class Solution:
    def countPaths(self, A: List[List[int]]) -> int:
        m, n, mod, dirs = len(A), len(A[0]), (10 ** 9) + 7, [(0, 1), (1, 0), (-1, 0), (0, -1)]
        @cache
        def dp(i, j):
            return sum((1 + dp(i + x, j + y)) for x, y in dirs if 0 <= i + x < m and 0 <= j + y < n and A[i + x][j + y] > A[i][j]) % mod
        return (sum(dp(i, j) % mod for i in range(m) for j in range(n)) + (m * n)) % mod