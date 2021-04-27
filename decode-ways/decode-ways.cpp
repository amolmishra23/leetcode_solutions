class Solution {
public:
    int numDecodings(string s) {
        int n = s.size();
        vector<int> mem(n+1, -1);
        mem[n] = 1;
        return n == 0 ? 0: solve(0, s, mem);
    }
    
    int solve(int i, string &s, vector<int> &mem) {
        // Either we are at end of string, or we have already computed it
        if (mem[i]>-1) return mem[i];
        // Basically stop here, because we cant have anything start with 0
        if (s[i]=='0') return mem[i]=0;
        
        // the case where we consider for single digit strings. like 1/2/3... this particular permutation is considered.
        int res = solve(i+1, s, mem);
        
        // for considering 2 letter strings
        if(i<s.size()-1 && (s[i]=='1'||s[i]=='2' && s[i+1]<'7')) res+=solve(i+2, s, mem);
        
        return mem[i] = res;
    }
};