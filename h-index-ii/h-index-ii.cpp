class Solution {
public:
    int hIndex(vector<int>& arr) {
        /*
        Description is pretty complex to understand.
        h index value is the number where arr[hindex] == arr.size() - hindex (as exactly N - h values are there with value less than h)
        It is possible to not have an exact number which is our h index but a number in between 2 values.
        The array is sorted. So we solve it using the binary search
        */
        if (arr.size()==0) {
            return 0;
        }
        
        int low(0), high(arr.size()-1), n(arr.size()), mid;
        
        while (low<=high) {
            mid = (low+high)>>1;
            if (arr[mid]==n-mid) {
                return arr[mid];
            } else if (arr[mid]>n-mid) {
                high = mid-1;
            } else {
                low = mid+1;
            }
        }
        
        // number of elements remaining after the high. That is basically the h-index
        // in an ideal world answer would have been, if arr[mid]==n-mid. So we assume n-mid as answer. 
        return n-low;
    }
};