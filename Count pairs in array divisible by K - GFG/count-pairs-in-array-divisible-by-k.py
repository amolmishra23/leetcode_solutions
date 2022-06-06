#User function Template for python3

class Solution:
    def countKdivPairs(self, arr, n, k):
        #code here
        # We have possibility of k numbers if we do modulus. 
        freq = [0]*k
        for num in arr:
            freq[num%k] += 1
        
        # if we have 2 numbers whose mod is 0, we can generate 1 pair out of it. 
        res = freq[0] * (freq[0]-1)//2
        
        # calculating how many pairs we can generate with the required sum 
        i = 1
        while (i<=k//2 and i!=(k-i)):
            res += (freq[i] * freq[k-i])
            i += 1
            
        # only if number is even, we can have same logic as with mod 0. 
        if k%2==0:
            res += freq[k//2] * (freq[k//2]-1)//2
            
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = int(input())
        ob= Solution()
        print(ob.countKdivPairs(a,n,k))
# } Driver Code Ends