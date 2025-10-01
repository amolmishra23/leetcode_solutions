class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        curr_full, curr_empty = numBottles, 0
        res = 0
        
        while curr_full:
            res += curr_full
            curr_empty += curr_full
            curr_full, curr_empty = divmod(curr_empty, numExchange)
            
        return res