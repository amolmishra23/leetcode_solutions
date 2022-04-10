class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.arr = encoding 
        self.idx = 0

    def next(self, n: int) -> int:
        while self.idx < len(self.arr):
            if n<=self.arr[self.idx]:
                self.arr[self.idx] -= n
                return self.arr[self.idx+1]
            n-=self.arr[self.idx]
            self.idx += 2
        return -1
            


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)