class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        if (nums.size()==0)
            return 0;
        if (nums.size()==1)
            return nums[0];
        
        int max_val = *max_element(nums.begin(), nums.end());
        
        vector<int> counter(max_val+1, 0), dp(max_val+1, 0);
        
        for (int &i: nums)
            counter[i]+=1;
        
        int res = 0;
        
        if (nums[1]!=0){
            dp[1] = counter[1];
            res = counter[1];
        }
        
        for (int i=2; i<max_val+1; i++) {
            if (counter[i] == 0)
                dp[i] = dp[i-1];
            else
                dp[i] = max(dp[i-1], dp[i-2]+i*counter[i]);
            res = max(res, dp[i]);
        }
        return res;
    }
};