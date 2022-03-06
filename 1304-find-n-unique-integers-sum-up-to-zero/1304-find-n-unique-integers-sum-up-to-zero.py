class Solution:
    def sumZero(self, n: int) -> List[int]:
        # We aim to form integers like -2,-1,0,1,2. 
        # If n is odd, we include 0
        # Else we dont include 0
        return [i for i in range(-(n//2), n//2+1) if not (i==0 and n%2==0)]