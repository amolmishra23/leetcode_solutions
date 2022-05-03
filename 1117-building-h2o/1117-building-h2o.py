from threading import Barrier, Semaphore
class H2O:
    def __init__(self):
        self.b = Barrier(3)
        self.h = Semaphore(2)
        self.o = Semaphore(1)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        """
        The whole idea here is that, so many people are firing the function call
        We need to just block it in a way that 2H,1O can be fired at once, to form a molecule.
        Hence using semaphore(2), for 2 H molecules to enter. Then a barrier for all 3 to enter at once. 
        """
        self.h.acquire()
        self.b.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.h.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o.acquire()
        self.b.wait()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.o.release()