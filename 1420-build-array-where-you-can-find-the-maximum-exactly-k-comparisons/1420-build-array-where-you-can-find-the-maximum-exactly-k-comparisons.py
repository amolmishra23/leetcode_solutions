class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        """
        Intent is to provide number of valid sequences such that
        1. We have "n" numbers sequence
        2. We have values between 1 to "m"
        3. We have "k" elements long increasing sub-sequence
        
        Solution is to try every possible sequence that starts with values from 1 to "m"
        And within each sequence, we again take numbers from 1 to "m"
        And each step accordingly we keep state of number of elements in sequence, and length of increasing subsequence
        
        In the base case, if we reach sequence of n numbers. With k comparisions, is success. Return 1
        Else if k is exhaused prior itself. Its failure. Return 0
        
        Answer will be very big. So return it modded. 
        """
        MOD = (10**9)+7
        
        @lru_cache(None)
        def dp(i, max_, k):
            if k<0: return 0
            if i==n: return k==0
            
            res = 0
            for j in range(1, m+1):
                res = (res + dp(i+1, max(max_, j), k-(j>max_))) % MOD
                
            return res
        
        return dp(0, float("-inf"), k)
#         res = 0
#         for i in range(1, m+1):
#             res = (res + dp(1, i, k-1)) % MOD
            
#         return res