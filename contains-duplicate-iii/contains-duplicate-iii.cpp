class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        if (nums.size() < 2 || k < 1 || t < 0) {
            return false;
        }
        
        multiset<long long> window;
        for (int i = 0; i < nums.size(); ++i) {
            if (i > k) {
                window.erase(window.find(nums[i - k - 1]));
            }
			
            window.insert(nums[i]);
            auto it = window.find(nums[i]);
			
            // when we inserted 9, we are checking if 9-5=4 <=3 no. 
            if (it != window.begin() && abs(*prev(it) - *it) <= t) {
                return true;
            }
            
            // when we inserted 9, if its not last elem, we check diff with its next elem. 
            if (next(it) != window.end() && abs(*it - *next(it)) <= t) {
                return true;
            }
        }
        return false;
    }
};