#include <string>
class Solution {
public:
    string getHint(string secret, string guess) {
        vector<int> count(10);
        int bull = 0, cow=0;
        
        for (int i=0; i<secret.size(); i++) {
            if (secret[i] == guess[i])
                bull += 1;
            else{
                count[secret[i]-'0'] += 1;
                count[guess[i]-'0'] -= 1;
            }   
        }
        
        for (int x: count){
            if (x>0){
                cow+=x;
            }
        }
        
        string res = to_string(bull)+"A"+to_string(secret.size()-bull-cow)+"B";
        return res;
    }
};