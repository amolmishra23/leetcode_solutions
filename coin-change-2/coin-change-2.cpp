class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<vector<int>> dp(coins.size()+1, vector<int>(amount+1));
        
        for(int i=0; i<=coins.size(); i++) { // iterating over the coins array
            for (int j=0; j<=amount; j++) { // we try to make all possible denominations (0 to target_amount)
                if (i==0 && j==0) // 0 coins and 0 target
                    dp[i][j]=1;
                else if (i==0) // no coins available
                    dp[i][j] = 0;
                else if (j==0) // 0 target with whatever coin
                    dp[i][j] = 1;
                else if (coins[i-1]<=j)
                    // excluding what best we can do
                    // including what best we can do
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]];
                else
                    dp[i][j] = dp[i-1][j]; // exluding this coin, the best we can do with other coins
            }
        }
        
        return dp[coins.size()][amount];
    }
};