class Solution:
    def numTrees(self, n: int) -> int:
        G = [0]*(n+1)
        # tree with 0 or 1 nodes, only 1 tree can be constructed. 
        G[0]=G[1]=1
        
        for i in range(2, n+1): # total number of nodes in the tree
            for j in range(1, i+1): # having the root as 1..i. All possibilities. 
                G[i] += G[j-1]*G[i-j] # F(3,7). Having 3 as root. Left subtree is (1,2) and right subtree is (4,5,6,7). So, boils down to G(2) and G(4)
        
        # Sum of all the possibilities are finally returned as G[n]
        return G[n]