# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        
        while low<=high:
            mid = low + (high-low)//2
            temp = guess(mid)
            if temp == 0: return mid
            # considering guess<num, and we need to search for bigger numbers
            elif temp > 0: low = mid + 1
            else: high = mid - 1
                
        return -1