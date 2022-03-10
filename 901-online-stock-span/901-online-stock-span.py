class StockSpanner:
    """
    Classic example of nearest greater element to the left.
    Combined with dp approach, so that we dont have to traverse the entire array. 
    """
    def __init__(self):
        self.stk = []

    def next(self, price: int) -> int:
        res = 1
        
        # We can use the stack logic, but also need to cache number of elements we popped.
        # So in future when we pop stuff, we can be sure of count of things. 
        while self.stk and self.stk[-1][0]<=price: 
            res += self.stk.pop()[1]
        
        self.stk.append((price, res))
    
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)