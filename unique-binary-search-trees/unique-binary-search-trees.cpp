class Solution {
public:
    int numTrees(int n) {
        vector<int> G(n+1, 0);
        // if the tree has only 0 or 1 nodes, we can construct just 1 tree
        G[0] = 1;
        G[1] = 1;
        
        for (int i=2; i<=n;i++) { //total number of nodes in the tree
            for (int j=1; j<=i; j++) { // putting each node as the root of the tree
                G[i] += G[j-1]*G[i-j]; // F(3,7). Having 3 as root of the tree. Left subtree is (1,2) And right subtree would contain (4,5,6,7). Which basically comes down to trees with 2 nodes and 4 nodes. Which again is a sub problem. Whose result we should have calculated in the previous step. 
            }
        }
        
        return G[n];
    }
};