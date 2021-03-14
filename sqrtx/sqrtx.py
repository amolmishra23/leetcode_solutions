class Solution:
    def mySqrt(self, x: int) -> int:
        """
        We do it in logn, using binary search
        """
        if x<2: return x
        
        low, high = 1, x//2
        
        while low<=high:
            mid = low + (high-low)//2
            
            if mid > x/mid: high = mid-1
            else: low = mid+1
            
        return low-1