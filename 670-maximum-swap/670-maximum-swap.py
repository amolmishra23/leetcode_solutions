class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        In order to perform maximum swap, we need to find biggest value index. 
        And swap it with the smallest number possible on its left.
        Something like 2736, 7 is biggest number. And the last min number on its left is, 2. So swap them both. 
        For input of 21736, the output would be 71236
        """
        digits = list(str(num))
        n = len(digits)
        max_idx = n-1
        left, right = 0, 0
        
        for i in range(n-2, -1, -1):
            """
            2 things to find out.
            1. max element
            2. left_most index smaller than max element
            
            So we keep comapring curr max element. 
            After finding max element as we go left, we keep updating the last ith element
            to swap it in the end. 
            """
            if digits[i]>digits[max_idx]:
                max_idx = i
            elif digits[max_idx]>digits[i]:
                left, right = i, max_idx
        
        digits[left], digits[right] = digits[right], digits[left]
        return int(''.join(digits))