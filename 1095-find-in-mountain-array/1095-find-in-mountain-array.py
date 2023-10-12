# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, A: 'MountainArray') -> int:
        n = A.length()
        
        l, r = 0, n-1
        peak = None
        
        while l<r:
            m = l + (r-l)//2
            if A.get(m) < A.get(m+1):
                l = peak = m+1
            else:
                r = m
                
        l, r = 0, peak
        while l<=r:
            m = l + (r-l)//2
            if A.get(m) < target:
                l = m+1
            elif A.get(m) > target:
                r = m-1
            else:
                return m
        
        l, r = peak, n-1
        while l<=r:
            m = l + (r-l)//2
            if A.get(m) > target:
                l = m+1
            elif A.get(m) < target:
                r = m-1
            else:
                return m
            
        return -1