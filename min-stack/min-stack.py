class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.min_val = None

    def push(self, x: int) -> None:
        if not self.stk:
            self.stk.append(x)
            self.min_val = x
        elif x>self.min_val:
            self.stk.append(x)
        else:
            temp = 2*x-self.min_val
            self.stk.append(temp)
            self.min_val = x

    def pop(self) -> None:
        if not self.stk: return -1
        if self.stk[-1]<self.min_val:
            temp = self.min_val
            self.min_val = 2*self.min_val - self.stk.pop()
            return temp
        else:
            return self.stk.pop()

    def top(self) -> int:
        if not self.stk: return -1
        
        return self.min_val if self.stk[-1]<self.min_val else self.stk[-1]
    

    def getMin(self) -> int:
        return -1 if not self.stk else self.min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()