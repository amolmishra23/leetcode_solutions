class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        n_sum = lambda x: (x*(x-1)//2)+1
        
        def calc(val, slots):
            res = 0
            
            if val>slots:
                res = n_sum(val) - n_sum(val-slots)
            else:
                res = n_sum(val)
                res += (slots-val)
            
            return res
        
        low, high = 1, maxSum
        left_slots, right_slots = index, n-index-1
        res = None
        
        while low<=high:
            mid = low + (high-low)//2
            
            left_sum = calc(mid, left_slots)
            right_sum = calc(mid, right_slots)
            total_sum = left_sum + right_sum + mid
            
            if total_sum > maxSum:
                high = mid-1
            else:
                res = mid
                low = mid+1
        
        return res