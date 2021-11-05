class Solution:
    """
    This is an arithmetic sequence. To find the sum S of an arithmetic series , the formula is :
    S = ((a + b)* h) /2
    Where:
    a is the number of coins on the first line
    b is the number of coins of the last line
    h is the number of lines we have (we want to find h)
    We note that a is always 1 because we start with one coin
    Therefore a = 1
    Note that the number of coins on the last line is always the same as the the number of total lines.
    Therefore: b = h
    The equation can then be simplified into:
    S = (1 + h)*h / 2
    Since we want only full lines, we want the sum S to be smaller than n, the total amount of coins in the question.
    Therefore:
    (1 + h)*h / 2 <= n
    """
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        
        while left<=right:
            mid = left + (right-left)//2
            curr = mid * (mid+1)//2
            
            if curr==n: return mid
            elif curr<n: left = mid+1
            else: right = mid-1
                
        return right
            