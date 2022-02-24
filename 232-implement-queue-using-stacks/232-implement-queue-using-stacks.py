class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stk1, self.stk2 = [], []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.stk1:
            self.stk2.append(self.stk1.pop())
        self.stk1.append(x)
        while self.stk2:
            self.stk1.append(self.stk2.pop())
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stk1.pop() if self.stk1 else -1
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stk1[-1] if self.stk1 else -1

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stk1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()