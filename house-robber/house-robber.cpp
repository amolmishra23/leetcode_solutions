class Solution {
public:
    int solve(vector<int>& nums, int idx, vector<int>& dp) {
        if (idx<0)
            return 0;
        if (dp[idx]>=0)
            return dp[idx];
        // either we can steal from 2 homes before+this house.
        // or skip this house and steal from 1 house before. 
        // that gives us the most optimized answer till that house.n 
        dp[idx] = max(solve(nums, idx-2, dp)+nums[idx], solve(nums, idx-1, dp));
        return dp[idx];
    }
    
    int rob(vector<int>& nums) {
        vector<int> dp(nums.size(), -1);
        return solve(nums, nums.size()-1, dp);
    }
};