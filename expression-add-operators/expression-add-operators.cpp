class Solution {
public:
    vector<string> res;
    void solve(string str, int idx, string temp, long long last, long long value, int target) {
        if (idx==str.size()) {
            // if we have reached end of string, and also our curr sum(value) is same as target, we add it to our res
            if (value==target)
                res.push_back(temp);
            return;
        }
        
        // intent is, to perform MCM
        // at every index, we try to break the string, and recur for the remaining string. 
        // at every break, we apply every possible operation. 
        // finally if any tree branch, gives us target, add it to result. 
        
        for (int i=idx; i<str.size(); i++) {
            // from idx, we need substrings of length 1,2...
            string s = str.substr(idx, i-idx+1);
            
            // to skip the cases, where first character is 0.
            if (s.size()>1 and s[0]=='0')
                return;
            
            // used to convert string to long data type. 
            long long curr = stoll(s);
            
            // takes care of all the cases like in 105, we need to do with 1, 10, 105 etc. Because temp would be empty in the 1st iteration
            if (temp.empty()){
                solve(str, i+1, temp+s, curr, curr, target);
            }// from 2nd iteration onwards, we need to apply all possible operators and find all the results.
            else {
                solve(str, i+1, temp+"+"+s, curr, value+curr, target);
                solve(str, i+1, temp+"-"+s, -curr, value-curr, target);
                // in case of 232, 2+3 is 5. if we wanna calculate 2+3*2 => its actually 8. But based on usual approach will give us res as 10. Hence to mitigate that, we subtract res-last_op_value and add curr*last_op_value. 
                solve(str, i+1, temp+"*"+s, curr*last, (value-last)+(curr*last), target);
            }
            
        }
    }
    

    vector<string> addOperators(string num, int target) {
        solve(num, 0, "", 0, 0, target);
        return res;
    }
/*
Suppose we have a string s = "232" and you want result as 8

Now what you choose is
"""
["23 +2", "2 + 32"]
"""

Suppose we have processed string as 2 + 3, the total value will be 5 and the last value is 3
Now if we want to place a multiplication operator then our string will be "2+3*2", where our value was 5 and we multiply it by 2, which will give us result as 10.
We want to remove the contribution It gets by some previous operations, Now if we have value = 5 and we are subtracting 3 , which means value = 2

Value = 2 + last_elementcurrent_value
= 2 + 32
= 8

We just dont want any contribution, if we have, so you check if the last value was 0 , then there is no contribution but if the last value was more than 1, then you must be sure there is some contribution from the previous call which you want to remove.

Do let me know, If it still Unclear.
*/

    
};