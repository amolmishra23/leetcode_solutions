class MinStack:

    def __init__(self):
        self.stk, self.min = [], None

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk.append(val)
            self.min=val
        elif val>self.min:
            self.stk.append(val)
        else:
            temp = 2*val - self.min
            self.stk.append(temp)
            self.min = val

    def pop(self) -> None:
        if not self.stk: return -1
        elif self.stk[-1]>self.min: return self.stk.pop()
        else:
            temp = self.min
            self.min = 2*self.min - self.stk.pop()
            return temp

    def top(self) -> int:
        if not self.stk: return -1
        
        return self.min if self.stk[-1]<self.min else self.stk[-1]

    def getMin(self) -> int:
        return -1 if not self.stk else self.min        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()