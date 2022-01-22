class Solution {
public:
    vector<int> prefix_sum;
    vector<vector<int>> memo;
    
    int solve(vector<int>& S, int s, int e) {
        // base condition in recursion
        if (s>e) {
            return 0;
        }
        
        if (memo[s][e]!=-1) {
            return memo[s][e];
        }
        
        memo[s][e] = 0;
        
        // try to break array at every possible point.
        for (int i=s; i<=e; i++) {
            //prefix sum logic to find left and right subarray sums
            int l = prefix_sum[i+1]-prefix_sum[s], r = prefix_sum[e+1]-prefix_sum[i+1];
            
            // if left is less than right, definitely current player will destroy right
            // and left gets added to opponent score.
            // we make the recursion accordingly for [start, break_point] of array
            if (l<r) {
                memo[s][e] = max(memo[s][e], l+solve(S, s, i));
            } else if (r<l) {
                memo[s][e] = max(memo[s][e], r+solve(S, i+1, e));
            } else {
                // here because their sums are equal we explore both possibilities before concluding
                memo[s][e] = max(memo[s][e], l+max(solve(S, s, i), solve(S, i+1, e)));
            }
        }
        
        return memo[s][e];
    }
    
    int stoneGameV(vector<int>& S) {
        memo.resize(S.size(), vector<int>(S.size(), -1));
        prefix_sum.resize(S.size()+1, 0);
        
        for (int i=0; i<S.size(); i++) {
            prefix_sum[i+1] = prefix_sum[i] + S[i];
        }
        
        return solve(S, 0, S.size()-1);
    }
};