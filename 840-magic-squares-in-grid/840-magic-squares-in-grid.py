class Solution(object):
    def numMagicSquaresInside(self, g):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def is_magic(i, j):
            s = "".join(
                str(g[i+x//3][j+x%3]) for x in [0,1,2,5,8,7,6,3]
            )
            return g[i][j]%2==0 and (
                s in "43816729"*2 or s in "43816729"[::-1]*2
            )
        
        m, n = len(g), len(g[0])
        return sum(
            is_magic(i, j) for i in range(m-2) for j in range(n-2) if g[i+1][j+1]==5
        )