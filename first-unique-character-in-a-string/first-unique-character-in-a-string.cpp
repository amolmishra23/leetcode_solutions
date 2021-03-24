#include <bits/stdc++.h>

class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char, int> m1;
        for (char c: s)
            m1[c]++;
        
        for (int i=0; i<s.length(); i++)
        {
            if (m1[s[i]]==1)
            {
                return i;
            }
        }
        
        return -1;
    }
};