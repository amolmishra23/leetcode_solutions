class Solution {
public:
    int helper(vector<int> &nums, int low, int high) {
        if (low == high) {
            return low;
        }
        int mid1 = low+(high-low)/2;
        int mid2 = mid1+1;
        if (nums[mid1]>nums[mid2]) {
            return helper(nums, low, mid1);
        } else {
            return helper(nums, mid2, high);
        }
    }
    
    int findPeakElement(vector<int>& nums) {
        return helper(nums, 0, nums.size()-1);
    }
};