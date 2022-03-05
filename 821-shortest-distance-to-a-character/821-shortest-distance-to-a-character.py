class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        n = len(S)
        res = [None]*n
        
        p = n-1
        
        for i in range(n):
            if S[i]==C: p = i
            res[i] = abs(p-i)
        
        p = 0
        for i in range(n-1, -1, -1):
            if S[i]==C: p=i
            res[i] = min(res[i], abs(p-i))
        
        return res