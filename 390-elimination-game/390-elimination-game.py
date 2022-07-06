class Solution:
    def lastRemaining(self, n: int) -> int:
        """
        Clear explanation given in: https://leetcode.com/problems/elimination-game/discuss/355060/C%2B%2B-simple-explanation-with-pictures
        We just need to find the last element left
        We track it using head.
        Head changes in only certain conditions. And next head can be determined by step. 
        If starting from left, head definitely changes
        If starting from right, head doesnt change, if count is even. Else it also changes by step
        Every iteration, step doubles, and count of elements halves. 
        """
        head, step = 1, 1
        d = True
        while n>1:
            if d: head += step
            else: head += 0 if n%2==0 else step
            step *= 2
            n //= 2
            d = not d
        return head