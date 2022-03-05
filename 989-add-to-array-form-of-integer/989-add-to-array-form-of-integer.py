class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        n = len(A)
        A.reverse()
        carry, i = K, 0
        
        A[i]+=carry
        carry, A[i] = divmod(A[i], 10)
        
        while carry:
            i+=1
            if i<n: A[i]+=carry
            else: A.append(carry)
            carry, A[i] = divmod(A[i], 10)
        
        A.reverse()
        return A