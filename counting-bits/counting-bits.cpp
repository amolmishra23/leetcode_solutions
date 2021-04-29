class Solution {
public:
    vector<int> countBits(int num) {
        if (num==0) {
            return vector<int>{0};
        }
        if(num==1) {
            return vector<int>{0,1};
        }
        vector<int> res(num+1);
        res[0] = 0;
        res[1] = 1;
        
        for (int i=2; i<=num; i++) {
            res[i] = i%2 ? res[i/2]+1 : res[i/2];
        }
        
        return res;
    }
};