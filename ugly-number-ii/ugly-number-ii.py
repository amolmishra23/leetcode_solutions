class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        We maintain 3 parallel pointers, in order to find the sorted list of multiples of 2,3,5
        Every point we try to multiply with all multiples 2,3,5. Whichever is smallest, that adds up to our sorted list.
        And we increment the counter t2/t3/t5 accordingly. So that we use that in next iteration.         
        As we reach nth number that happens to be our answer. 
        """
        if n<=0: return false
        if n==1: return 1
        t2, t3, t5 = 0, 0, 0
        
        dp = [None]*n
        dp[0] = 1
        
        for i in range(1, n):
            dp[i] = min(2*dp[t2], 3*dp[t3], 5*dp[t5])
            
            if dp[i] == 2*dp[t2]: t2+=1
            if dp[i] == 3*dp[t3]: t3+=1
            if dp[i] == 5*dp[t5]: t5+=1
                
        return dp[n-1]
        