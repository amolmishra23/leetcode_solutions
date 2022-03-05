class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(A), len(A[0])
        
        for i in range(m):
            for j in range(n//2 if n%2==0 else n//2+1):
                k = n-1-j
                A[i][j], A[i][k] = abs(A[i][k]-1), abs(A[i][j]-1)
                
        return A
                