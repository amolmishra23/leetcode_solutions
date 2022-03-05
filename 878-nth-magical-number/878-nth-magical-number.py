class Solution:
    def nthMagicalNumber(self, N, A, B):
        """
        We solve this problem using binary search. 
        Keep finding the mid number, and check it is which'th magical number. 
        And based on if its less than N, surely our num lies in (mid+1, end)
        Else it will lie in (low, mid-1)
        """
        lcm, Q = A*B//gcd(A,B), 10**9 + 7
        
        beg, end = 0, N * min(A,B)
        while beg < end:
            mid = (beg + end)//2
            if mid//A + mid//B - mid//lcm < N:
                beg = mid + 1
            else:
                end = mid
        
        return beg % Q