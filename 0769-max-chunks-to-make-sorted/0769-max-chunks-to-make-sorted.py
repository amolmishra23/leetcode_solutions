class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        Algorithm: Iterate through the array, each time all elements to the left are smaller (or equal) to all elements to the right, there is a new chunck.
Use two arrays to store the left max and right min to achieve O(n) time complexity. 
Space complexity is O(n) too.
This algorithm can be used to solve ver1 too.

        """
        
        n = len(arr)
        max_left, min_right = [None]*n, [None]*n
        
        max_left[0], min_right[-1] = arr[0], arr[-1]
        
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], arr[i])
            
        for i in range(n-2, -1, -1):
            min_right[i] = min(min_right[i+1], arr[i])
            
        res = 0
        for i in range(n-1):
            if max_left[i]<=min_right[i+1]:
                res += 1
                
        return res+1
        