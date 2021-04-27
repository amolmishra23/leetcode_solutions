class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int lowest = INT_MAX;
        int max_profit = 0;
        
        /*
        We need atleast 2 transactions to make a profit. 
        Sell on lower day, and sold on highest day.
        So we first need to find the best possible lowest day.
        And then keep seeing selling on which day would fetch us maximum possible profit.
        */
        for (int i=0; i<prices.size(); i++) {
            if (prices[i]<lowest) lowest = prices[i];
            else max_profit = max(max_profit, prices[i]-lowest);
        }
        
        return max_profit;
    }
};