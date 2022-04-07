class Solution:
    def numTrees(self, n: int) -> int:
        G = [0]*(n+1)
        
        G[0] = G[1] = 1
        
        for i in range(2, n+1):
            # we can have both 1, 2 as roots
            # if 1 is root, left side will have G[1-0] nodes and right side will have G[2-1] nodes. 
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]
                
        return G[-1]