class Solution {
public:
    int integerBreak(int n) {
        if (n<=2)
            return 1;
        
        vector<int> res(n+1, 0);
        
        res[1] = 1;
        // because 2 can be just split as 1+1. And 1*1 is 1. 
        res[2] = 1;
        
        for (int i = 3; i<=n; i++) {
            for (int j=1; j<i; j++) {
                /*
                Either we use the number as is. Or can split and use it 
                5 = 2*func(3);
                2*1*2 = 4
                2*3 = 6
                To support the second case, we add it as j*(i-j)
                */
                res[i] = max(res[i], max(j*res[i-j], j*(i-j)));
            }
        }
        
        return res[n];
    }
};