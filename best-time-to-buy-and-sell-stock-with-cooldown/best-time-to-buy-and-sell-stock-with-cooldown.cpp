/*
dp[len][2]
case 1: We have a stock on day i
** We purchased it today. To purchase today, we should have not sold yesterday(cooldown of 1 day)
dp[i-2][0] - prices[i]
** We just carry forwarding
dp[i-1][1]

case 2: We have no stock on day i
** We just sold the stock today. 
dp[i-1][1]+prices[i]
** We just carry forwarding
dp[i-1][0]
*/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int len = prices.size();
        
        // we can make no profit essentially
        if (len<=1) return 0;
        
        // either we dont do a transaction or just buy on day 0 and sell on day 1
        if (len==2) return max(0, prices[1]-prices[0]);
        
        vector<vector<int>> dp(len, vector<int>(2));
        
        // hereafter 0 would denote we dont hold a stock. 1 we hold a stock.
        
        dp[0][0] = 0;
        dp[0][1] = -prices[0];
        // if not holding stock on day 1, means sold on day 1, after buying on day 0. 
        dp[1][0] = max(dp[0][0], dp[0][1]+prices[1]);
        // if holding stock on day 1, either carry forward from day 0, or buying on day 1
        dp[1][1] = max(dp[0][1], dp[0][0]-prices[1]);
        
        
        for(int i=2; i<len; i++) {
            // just substituting the values we mentioned above. 
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]);
            dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i]);
        }
        
        return dp[len-1][0];
    }
};