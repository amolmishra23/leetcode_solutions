class Solution:
    @lru_cache(None)
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1: return 0 if k==1 else 1
        
        # total number of elements in a row is 2**(n-1)
        # if it lies in first half, we just find the element in previous row
        # if it lies in second half, we inverse and find the element in previous row
        N = 2**(n-1)
        
        if k<=N//2: return self.kthGrammar(n-1, k)
        else: return 1 - self.kthGrammar(n-1, k-(N//2))
        