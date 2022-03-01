class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        After we sort, the only aim is, to validate if particular person's expectation is less than cookie.
        Number of persons we have traversed is the answer. 
        If we couldnt traverse a person, we drop there, and return the number of people. 
        """
        g.sort()
        s.sort()
        
        i, j, = 0, 0
        
        while i<len(g) and j<len(s):
            if g[i] <= s[j]:
                i+=1
                j+=1
            else:
                j+=1
                
        return i