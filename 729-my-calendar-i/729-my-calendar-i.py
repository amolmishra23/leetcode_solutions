import bisect

"""
A very interesting bisect package in python. 
Used to binary search and return the index to insert an element, so that array remains sorted. 
The logic is if we try to insert the time range, in case the insertion index is odd, means its not disturbing any other time ranges. 
And both start and end have to be inserted at same time range for time being. 
If thats possible, return True or return a collision. 
"""

class MyCalendar:
    def __init__(self):
        self.ts = []
    
    def book(self, start, end):
        st = bisect.bisect(self.ts, start)
        et = bisect.bisect_left(self.ts, end)
        if st%2 or et%2 or st!=et:
            return False
        self.ts.insert(st, start)
        self.ts.insert(st+1, end)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)