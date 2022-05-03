from threading import *

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.cur = 1
        self.cond = Condition()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            with self.cond:
                self.cond.wait_for(lambda: self.cur > self.n or (self.cur % 3 == 0 and self.cur % 5 != 0))
                if self.cur > self.n:
                    return
                printFizz()
                self.cur += 1
                self.cond.notify_all()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
    	    with self.cond:
                self.cond.wait_for(lambda: self.cur > self.n or (self.cur % 3 != 0 and self.cur % 5 == 0))
                if self.cur > self.n:
                    return
                printBuzz()
                self.cur += 1
                self.cond.notify_all()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.cond:
                self.cond.wait_for(lambda: self.cur > self.n or (self.cur % 3 == 0 and self.cur % 5 == 0))
                if self.cur > self.n:
                    return
                printFizzBuzz()
                self.cur += 1
                self.cond.notify_all()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.cond:
                self.cond.wait_for(lambda: self.cur > self.n or (self.cur % 3 != 0 and self.cur % 5 != 0))
                if self.cur > self.n:
                    return
                printNumber(self.cur)
                self.cur += 1
                self.cond.notify_all()