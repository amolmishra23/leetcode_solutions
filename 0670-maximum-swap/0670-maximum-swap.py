class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        n = len(digits)
        max_idx = n-1
        left, right = 0, 0
        
        for i in range(n-2, -1, -1):
            if digits[i] > digits[max_idx]:
                max_idx = i
            elif digits[max_idx] > digits[i]:
                left, right = i, max_idx
                
        digits[left], digits[right] = digits[right], digits[left]
        return int("".join(digits))