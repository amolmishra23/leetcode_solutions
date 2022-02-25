class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1: return True
        low, high = 0, num//2
        
        while low<=high:
            mid = low + (high-low)//2
            
            if mid*mid == num: return True
            elif mid*mid<num: low = mid+1
            else: high = mid-1
                
        return False