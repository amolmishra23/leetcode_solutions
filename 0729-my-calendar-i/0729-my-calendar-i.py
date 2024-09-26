class MyCalendar:

    def __init__(self):
        self.ts = []        

    def book(self, start: int, end: int) -> bool:
        st = bisect.bisect_right(self.ts, start)
        et = bisect.bisect_left(self.ts, end)
        if st%2 or et%2 or st!=et: return False
        self.ts.insert(st, start)
        self.ts.insert(st+1, end)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)