class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int res{0};
        auto row{strs.size()}, col{strs[0].size()};
        
        for(int j=0; j<col; j++)
        {
            for(int i=0; i<row-1; i++)
            {
                if(strs[i][j]>strs[i+1][j])
                {
                    res++;
                    break;
                }
            }
        }
        
        return res;
    }
};