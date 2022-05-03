from threading import Condition

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.ct = 0
        self.condition = Condition()
        self.order = 2
        
    def zero(self, printNumber):
        for _ in range(self.n):
            with self.condition:
                self.condition.wait_for(lambda: self.order == 2)
                printNumber(0)
                self.ct += 1
                self.order = self.ct % 2
                self.condition.notify(2)
        
    def even(self, printNumber):
        for _ in range(self.n//2):
            with self.condition:
                self.condition.wait_for(lambda: self.order == 0)
                printNumber(self.ct)
                self.order = 2
                self.condition.notify(2)
        
    def odd(self, printNumber):
        for _ in range((self.n+1)//2):
            with self.condition:
                self.condition.wait_for(lambda: self.order == 1)
                printNumber(self.ct)
                self.order = 2
                self.condition.notify(2)