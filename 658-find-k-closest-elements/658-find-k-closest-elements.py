class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        idx = bisect.bisect_left(arr, x) 
        
        left, right = max(0, idx - k), min(idx + k, len(arr) - 1)

        while right - left + 1 > k: 
            if x - arr[left] > arr[right] - x: 
                left += 1
            else:
                right -= 1
        
        return arr[left: right + 1]