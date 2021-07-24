class Solution {
public:
    vector<string> res;
    void solve(string str, int idx, long long last_num, long long curr_sum, int target, string curr_str) {
        if (idx>=str.size()) {
            if (curr_sum==target) {
                res.push_back(curr_str);
                return;
            }
        }
        // intent is, to perform MCM
        // at every index, we try to break the string, and recur for the remaining string. 
        // at every break, we apply every possible operation. 
        // finally if any tree branch, gives us target, add it to result. 
        
        for (int i=idx; i<str.size(); i++) {
            // initially i==idx, so 1 length will be chosen
            // eventually bigger substrings will be chosen upon. 
            string s = str.substr(idx, i-idx+1);

            if (s.size()>1 and s[0]=='0')
                return;
            
            long long curr = stoll(s);
            
            // takes care of all the cases like in 105, we need to do with 1, 10, 105 etc. Because temp would be empty in the 1st iteration
            if (curr_str.empty()) {
                solve(str, i+1, curr, curr, target, curr_str+s);
            } else {
                // from 2nd iteration onwards, we need to apply all possible operators and find all the results.
                solve(str, i+1, curr, curr_sum+curr, target, curr_str+"+"+s);
                solve(str, i+1, -curr, curr_sum-curr, target, curr_str+"-"+s);
                // in case of 232, 2+3 is 5. if we wanna calculate 2+3*2 => its actually 8. But based on usual approach will give us res as 10. Hence to mitigate that, we subtract res-last_op_value and add curr*last_op_value. 
                solve(str, i+1, (last_num*curr), (curr_sum-last_num)+(last_num*curr), target, curr_str+"*"+s);
            }
        }
    }
    vector<string> addOperators(string num, int target) {
        solve(num, 0, 0, 0, target, "");
        return res;
    }
};