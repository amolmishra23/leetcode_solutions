class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Basically need to sit and design a state machine for the problem.
        And come up with a solution. 
        """
        n = len(prices)
        
        # we can make no profit essentially
        if n <= 1: return 0
        
        # either we dont do a transaction, or just buy on day 0 and sell on day 1
        elif n==2: return max(0, prices[1]-prices[0])
        
        # we will have 2 values for each index
        # we are either holding a stock, or not holding a stock. 
        dp = [[0]*2 for _ in range(n)]
        
        # if we want to hold stock on day 1, we will loose money -prices[0]
        dp[0][0], dp[0][1] = 0, -prices[0]
        
        # in order to not hold stock on day 1, there are 2 ways:
        # maximum of, if we didnt buy both on day 0,1
        # if we buy on day 0, and sell it off on day 1
        dp[1][0] = max(dp[0][0], dp[0][1]+prices[1])
        
        # in order to hold stock on day 1, there are 2 ways:
        # carry forward the stock holding from day 0
        # buy stock on day 1, whatever we purchased on day 0
        dp[1][1] = max(dp[0][1], dp[0][0]-prices[1])
        
        
        # copy pasting the same above conditions. 
        for i in range(2, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
            
        return dp[n-1][0]