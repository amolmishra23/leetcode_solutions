class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        """
        One of the toughest solved till date
        """
        emptyL, emptyR = index, n-index-1

        l, r, res = 1, maxSum, 0
        natural_sum = lambda x: (x*(x+1))//2
        is_valid_sum = lambda x: x<=maxSum

        def find_sum(avlb, empty):
            res = 0
            if avlb >= empty:
                res = natural_sum(avlb) - natural_sum(avlb-empty)
            else:
                res = natural_sum(avlb) + (empty - avlb)
            return res

        while l<=r:
            m = l + (r-l)//2
            avlb = m-1
            left_sum, right_sum = find_sum(avlb, emptyL), find_sum(avlb, emptyR)
            total_sum = left_sum + m + right_sum
            if is_valid_sum(total_sum):
                res = m
                l = m+1
            else:
                r = m-1

        return res
            