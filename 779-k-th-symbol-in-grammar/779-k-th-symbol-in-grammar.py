class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        """
        Typical aditya verma recursion problem
        In Nth row, we can have total of 2**(N-1) elements
        
        if the element we are searching occurs in 1st half of prev row, its exact value
        if in second half, its the opposite of element present in 1st half
        Like this in recursion as we hit base case, (1,1) we get the result as 0 or 1. 
        """
        if N==1 and K==1: return 0
        
        n = 2**(N-1)
        
        if K<=n//2: return self.kthGrammar(N-1, K)
        else: return 1^self.kthGrammar(N-1, K-n//2)
        