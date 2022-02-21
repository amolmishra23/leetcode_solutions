class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        if len(arr)==1: return 0
        low, high = 0, len(arr)-1
    
        while low<=high:
            mid = low + (high-low)//2

            if mid==0: return 0 if arr[0]>arr[1] else 1
            elif mid==len(arr)-1: return mid if arr[mid]>arr[mid-1] else mid-1
            elif arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]: return mid
            elif arr[mid+1]>arr[mid-1]: low = mid+1
            else: high = mid-1

        return -1