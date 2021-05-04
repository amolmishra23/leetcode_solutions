class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum_ = accumulate(nums.begin(), nums.end(), 0);
        if (sum_%2 != 0)
            return false;
        
        sum_ = sum_/2;
        
        vector<vector<bool>> dp(nums.size()+1, vector<bool>(sum_+1));
        
        for (int i=0; i<=nums.size(); i++) {
            for (int j=0; j<=sum_; j++) {
                if (i==0 && j==0) {
                    dp[i][j] = true;
                } else if (i==0) {
                    dp[i][j] = false;
                } else if (j==0) {
                    dp[i][j] = true;
                } else if (nums[i-1]<=j) {
                    dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i-1]];
                } else {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        
        return dp[nums.size()][sum_];
    }
};