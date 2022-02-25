import bisect

class MyCalendarThree:

    def __init__(self):
        self.books = [[-1, 0]]
        self.max_ = 0

    def book(self, start: int, end: int) -> int:
        i = bisect.bisect(self.books, [start, float('inf')])
        if self.books[i-1][0]==start: i-=1
        else: self.books.insert(i, [start, self.books[i-1][1]])
        
        j = bisect.bisect(self.books, [end, float('inf')])
        if self.books[j-1][0]==end: j-=1
        else: self.books.insert(j, [end, self.books[j-1][1]])
        
        for k in range(i, j):
            self.books[k][1]+=1
            self.max_=max(self.max_, self.books[k][1])
        
        return self.max_


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)