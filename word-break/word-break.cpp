class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        if (wordDict.size()==0) return false;
        
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        
        vector<bool> dp(s.size()+1, false);
        /*
        dp[i] says if breaking the word from 0 to i-1, it exists in the dictionary
        lets say word is leetcode. i=4
        j=3
        j=2
        j=1
        j=0, this is true. 
        hence now we check if j=0 to 4 chars more is it available in dictionary
        As its leet, hence we will now make dp[4]=true
        */
        dp[0] = true;
        
        // we need to go to size+1 index
        for (int i=1; i<=s.size(); i++) {
            for (int j=i-1; j>=0; j--) {
                if (dp[j]) {
                    // from j, we need more i-j characters
                    string word = s.substr(j, i-j);
                    if (dict.find(word) != dict.end()) {
                        dp[i] = true;
                        break;
                    }
                }
            }
        }
        
        return dp[s.size()];        
    }
};