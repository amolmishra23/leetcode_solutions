class Solution {
public:
    int res = INT_MAX;
    int minSubArrayLen(int target, vector<int>& nums) {
        int window_start = 0, running_sum = 0;
        
        for (int i=0; i<nums.size(); i++) {
            running_sum += nums[i];
            
            while (running_sum>=target) {
                res = min(res, i-window_start+1);
                running_sum -= nums[window_start];
                window_start += 1;
            }
        }
        
        return res==INT_MAX ? 0 : res;
    }
};