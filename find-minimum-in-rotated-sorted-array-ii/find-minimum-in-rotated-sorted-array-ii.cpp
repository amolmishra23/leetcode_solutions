class Solution {
public:
    int findMin(vector<int>& nums) {
        int low = 0;
        int high = nums.size()-1;
        int mid = 0;
        
        while (low<high) {
            mid = low + (high-low)/2;
            
            if (nums[mid]>nums[high])
                // mid is surely not the answer. Hence mid+1
                low = mid+1;
            else if (nums[mid]<nums[high])
                // mis may be the answer still. Hence not mid-1.
                high = mid;
            else
                // assuming nums[mid]==nums[high]. Answer can be anywhere in between or just either of them. Hence move 1 by 1 index. 
                high-=1;
        }
        
        // the low pointer points to the minimum element in array
        return nums[low];
    }
};