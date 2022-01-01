class Solution {
public:
    int t[550][550];
    
    int solve(vector<int>& nums, int i, int j) {
        if (t[i][j]!=-1){
            return t[i][j];
        }
        
        if (i>=j) {
            return 0;
        }
        
        int res = 0;
        
        for (int k=i; k<j; k++) {
            res = max(res, 
                      solve(nums, i, k) + solve(nums, k+1, j)+ nums[i-1]*nums[k]*nums[j]);
        }
        
        t[i][j] = res;
        return res;
    }
    
    int maxCoins(vector<int>& nums) {
        nums.insert(nums.begin(), 1);
        nums.insert(nums.end(), 1);
        memset(t, -1, sizeof(t));
        return solve(nums, 1, nums.size()-1);
    }
};