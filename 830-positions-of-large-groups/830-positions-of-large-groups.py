class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        start, counter = 0, 1
        res = []
        n = len(s)
        for i in range(n):
            """
            At curr index we keep checking if next index is same
            If yes, we keep incrementing the counter variable.
            If no, we append the compressed thing. 
            """
            if i<n-1 and s[i]==s[i+1]: counter+=1
            else:
                if counter>=3: 
                    res.append([start, i])
                start, counter = i+1, 1
        return res