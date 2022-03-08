class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def maxSumSubarray(arr):
            sub_s_max = float('-inf')
            s_curr = 0
            prefix_sums = [float('inf')]
            for x in arr:
                """
                Intent here is, to insert the curr running sum in the array
                Now find the most optimal value to subtract, so as to get k
                Whatever is the nearest value to k, we keep updating in subarray max
                """
                bisect.insort(prefix_sums, s_curr)
                s_curr += x
                i = bisect.bisect_left(prefix_sums, s_curr - k)
                sub_s_max = max(sub_s_max, s_curr - prefix_sums[i])
            return sub_s_max
        
        m, n = len(matrix), len(matrix[0])
        
        # col wise we do prefix sum sort of thing.
        """
        First of all if our matrix is 
        1 1 1 1
        1 1 1 1
        1 1 1 1
        1 1 1 1
        We calculate the pre_sum column wise, and convert our matrix to
        1 2 3 4
        1 2 3 4
        1 2 3 4
        1 2 3 4
        """
        for x in range(m):
            for y in range(n - 1):
                matrix[x][y+1] += matrix[x][y]
        res = float('-inf')
        
        """
         Basic idea is, the sum is calculated in the following sequence
        1. [0..0], [0..1], [0..2], [0..3]
        2. [1..1], [1..2], [1..3]
        3. [2..2], [2..3]
        4. [3..3]
        
        This above was just columns, We also need to do across rows. Hence another iteration too. 
        """
        for y1 in range(n):
            for y2 in range(y1, n):
                arr = [matrix[x][y2] - (matrix[x][y1-1] if y1 > 0 else 0) for x in range(m)]
                res = max(res, maxSumSubarray(arr))
        return res