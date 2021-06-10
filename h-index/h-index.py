class Solution:
    def hIndex(self, arr: List[int]) -> int:
        if len(arr)==0: return 0
        
        arr.sort()
        
        low, high, n = 0, len(arr)-1, len(arr)
        
        """
        Example being [0,1,3,5,6]
        if arr[2]=3, means after that we have 3 more numbers left(n-mid). 
        3 is the h-index. 
        """
        while low<=high:
            mid = low + (high-low)//2
            if arr[mid] == n-mid: return arr[mid]
            elif arr[mid]>n-mid: high=mid-1
            else: low=mid+1
                
        return n-low