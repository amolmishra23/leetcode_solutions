class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        n = len(A)
        max_so_far = [None]*n
        max_so_far[0] = A[0]

        for i in range(1, n):
            max_so_far[i] = max(A[i], max_so_far[i-1])
        
        min_from_end = [None]*n
        min_from_end[-1] = A[n-1]
        
        for i in range(n-2, -1, -1):
            min_from_end[i] = min(A[i], min_from_end[i+1])
        
        for i in range(1, n):
            if max_so_far[i-1] <= min_from_end[i]: return i