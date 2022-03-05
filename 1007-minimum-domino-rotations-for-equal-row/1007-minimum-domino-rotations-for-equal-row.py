class Solution:
    def swaps(self, target, A, B):
        num_swaps = 0
        n = len(A)
        for i in range(n):
            if A[i]!=target and B[i]!=target: return float('inf')
            if A[i]!=target: num_swaps += 1
        
        return num_swaps
    
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        """
        Smart pythonic way of doing it. 
        
        intersect = reduce(set.__and__, [set(d) for d in zip(A, B)])
        if not intersect: return -1
        x = intersect.pop()
        return min(
            len(A)-A.count(x),
            len(B)-B.count(x)
        )
        """
        
        """
        The way to achieve it is, we either have entire 
        1. A array as A[0]
        2. B array as A[0]
        3. A array as B[0]
        4. B array as A[0]
        
        We need to find which of these gives us the minimum answer, and return it. 
        Because all of them, need to satisfy a condition, in between we can short circuit it. 
        """
        
        min_swaps = min([
            self.swaps(A[0], A, B), 
            self.swaps(B[0], A, B),
            self.swaps(A[0], B, A),
            self.swaps(B[0], B, A)
        ])
        return -1 if min_swaps == float('inf') else min_swaps
        
    