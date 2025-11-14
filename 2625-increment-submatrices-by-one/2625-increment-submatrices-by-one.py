class Solution:
    def rangeAddQueries(self, n, queries):
        # Step 1: Initialize difference matrix
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Step 2: Apply difference updates for each query
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1
        
        # Step 3: Compute prefix sums to build final matrix
        for i in range(n):
            for j in range(n):
                diff[i][j + 1] += diff[i][j]
        for j in range(n):
            for i in range(n):
                diff[i + 1][j] += diff[i][j]
        
        # Step 4: Extract n x n result
        result = [[diff[i][j] for j in range(n)] for i in range(n)]
        return result
