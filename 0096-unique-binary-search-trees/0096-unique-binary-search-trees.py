class Solution:
    def numTrees(self, n: int) -> int:
        G = [0]*(n+1)
        G[0] = G[1] = 1
        
        # we can considering when we have i nodes
        for i in range(2, n+1):
            # what if j is the root in the tree containing i nodes
            for j in range(i+1):
                G[i] += G[j-1] * G[i-j]
                
        return G[-1]