class Solution {
    unordered_map<string, vector<string>> m;
    
    vector<string> combine(string word, vector<string> prev) {
        for (int i=0; i<prev.size(); i++) {
            prev[i] +=" "+word;
        }
        return prev;
    }
    
public:
    vector<string> wordBreak(string s, vector<string>& dict1) {
        // checking if this string or substring is already been processed by us
        if(m.count(s)) return m[s];
        unordered_set<string> dict(dict1.begin(), dict1.end());
        
        /* 
        result of all the combinations for string s.
        catsand => ["cats and", "cat sand"]
        */
        vector<string> result;
        // if the word itself is present in worddict, add it to our result
        if(dict.count(s)) {
            result.push_back(s);
        }
        
        for (int i=1; i<s.size(); i++) {
            
            // checking if we break the word at i. is i to n-1 is a valid word in dict.
            // if it is valid word in dict. all we need to do is, append it to wordBreak result of 0 to i-1. 
            string word = s.substr(i);
            if (dict.count(word)) {
                string rem = s.substr(0, i);
                vector<string> prev = combine(word, wordBreak(rem, dict1));
                // as we find the result, we append the prev to result vector. 
                result.insert(result.end(), prev.begin(), prev.end());
            }
        }
        
        // cache the result before returning to the client. so that dont need to repeat it. 
        m[s] = result;
        return result;
    }
};