class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        """
        We keep traversing the array and caching in dict, so as for faster lookup.
        As soon as we find a number that is half or double the number we return True
        Else we return False
        """
        lookup = {}
        
        for a in arr:
            if (2*a in lookup) or (a%2==0 and a//2 in lookup): return True
            lookup[a] = True
        
        return False
            