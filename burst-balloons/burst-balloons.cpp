class Solution {
    
public:
    // A hash function used to hash a pair of any kind
    int t[550][550];
    
    int solve(vector<int>& nums, int i, int j) {
        if (t[i][j]!=-1){
            return t[i][j];
        }
        
        if (i>=j){
            return 0;
        }
        
        int max_ = 0;
        
        for (int k=i; k<=j-1; k++) {
            int a = solve(nums, i, k);
            int b = solve(nums, k+1, j);
            int c = nums[i-1]*nums[k]*nums[j];
            
            max_ = max(max_, a+b+c);
        }
        
        t[i][j] = max_;
        return t[i][j];
    }
    
    int maxCoins(vector<int>& nums) {
        nums.insert(nums.begin(), 1);
        nums.insert(nums.end(), 1);
        memset(t, -1, sizeof(t));
        return solve(nums, 1, nums.size()-1);
    }
};