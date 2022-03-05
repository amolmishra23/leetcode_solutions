class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        res, up, down = 0, 0, 0
        
        for i in range(1, n):
            # exit conditions if the down condition doesnt match
            # or if elements turn to be equal
            if (down and arr[i-1]<arr[i]) or (arr[i-1]==arr[i]):
                up, down = 0, 0
            
            # updating the count of up or down
            up += (arr[i-1]<arr[i])
            down += (arr[i-1]>arr[i])
            
            # updating the result
            if up and down: res = max(res, up+down+1)
        
        return res