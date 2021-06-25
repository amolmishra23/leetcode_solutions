class Solution:
    def climbStairs(self, n: int) -> int:
        """
        If 1 stair, we can only climb 1 way
        if 2 stairs, we can climb either 1+1 or we can climb 2. 
        For 3 stairs, we can either come from n-2(1) and n-1(2), whatever ways was possible until that. 
        Thats the speciality of only 3. We can reach from 1, 2. Hence add up the possible ways. 
        Like this we form the recursion tree and solve the question. 
        """
        if n<=2: return n
        dp = [None]*(n+1)
        dp[1], dp[2] = 1, 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
            
        return dp[n]