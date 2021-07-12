class Solution {
public:
    int ans = 0;  // Our main solution variable
	int LCS(vector<int>& s1, vector<int>& s2, int n, int m, vector<vector<int>> &memo){
        if(n >= s1.size() || m >= s2.size())        // base case, when one of the string becomes empty
            return 0;
        if(memo[n][m] != -1)        // if in our solution space(memo table) already have some value return it (except -1);
            return memo[n][m];
        
        LCS(s1, s2, n + 1, m, memo);
        LCS(s1, s2, n, m + 1, memo);
        
        if(s1[n] == s2[m]){
            memo[n][m] = 1 + LCS(s1, s2, n + 1, m + 1, memo);  // If letter in both strings are same then add one and recurr for next letter
            ans = max(ans, memo[n][m]);
            return memo[n][m];
        }
        return memo[n][m] = 0;  // when discontinuity of letters break, then again start with zero 
	}
    
    int findLength(vector<int>& s1, vector<int>& s2) {
		int n = s1.size(), m = s2.size();
		vector<vector<int>> memo(n + 1, vector<int>(m + 1, -1));
		LCS(s1, s2, 0,0, memo);
        return ans;
    }
};