class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1
        
        while l<r:
            m = l + (r-l)//2
            if arr[m]<arr[m+1]: l=m+1
            else: r = m
        
        return l