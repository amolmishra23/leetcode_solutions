class StockSpanner:

    def __init__(self):
        self.stk = []

    def next(self, price: int) -> int:
        res = 1
        
        while self.stk and self.stk[-1][0]<=price:
            res += self.stk.pop()[1]
            
        self.stk.append((price, res))
        
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)