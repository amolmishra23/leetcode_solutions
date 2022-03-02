class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        arr = [-float('inf')] + arr + [float('inf')]
        idx = bisect.bisect(arr,x)
        i, j = idx-1, idx
        
        while True:
            if abs(arr[i]-x) <= abs(arr[j]-x):
                i -= 1
            else:
                j += 1
            if j-i == k+1:
                return arr[i+1:j]