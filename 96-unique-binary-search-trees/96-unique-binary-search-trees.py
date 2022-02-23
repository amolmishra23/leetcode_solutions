class Solution:
    def numTrees(self, n: int) -> int:
        """
        Tricky question in terms of placement of nodes, in BST can be either ways
        In fact, if we have 3 nodes, we can generate 5 valid bst's
        To solve this we use the formula called catalan number. 
        
        If we are generating a bst with 7 nodes, and 3 is chosen as one of the roots. 
        Left subtree will have 2 nodes and right subtree with have 4 nodes. So again, we can recursively answer this question.
        """
        
        G = [0]*(n+1)
        
        # tree with 0 or 1 nodes, only 1 tree can be constructed. 
        G[0] = G[1] = 1
        
        for i in range(2, n+1): # total number of nodes in the tree
            for j in range(1, i+1): # having the root as 1..i. All possibilities. 
                # F(3,7). Having 3 as root. 
                # Left subtree is (1,2) and right subtree is (4,5,6,7). So, boils down to G(2) and G(4)
                G[i] += G[j-1] * G[i-j]
                
        return G[-1]