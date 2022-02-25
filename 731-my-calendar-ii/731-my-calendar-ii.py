"""
lets say we have the events [15,25] and [20, 30]
max(15,20) = 20
min(25, 30) = 25
because 20<25, meaning though 1 event was supposed to end at 25, we started event 2 at 20 itself. 
for event like [15, 20] [25, 30]
max(15, 25) = 25
min(20, 30) = 20
25<20 is false. hence there is no clash

Have 2 lists q1 and q2. 
q1 contains the first entry.
q2 contains the repeated entry for the particular time range. 
if something matches in q2, return False. 
check if something is clashing in q1. Only for the clashed part enter in q2. 
Add the entry in q1
"""

class MyCalendarTwo:

    def __init__(self):
        self.q1=[]
        self.q2=[]

    def book(self, start: int, end: int) -> bool:
        def is_booked(s, e):
            return max(s,start)<min(end, e)
        
        for s,e in self.q2:
            if is_booked(s, e):
                return False
        
        for s,e in self.q1:
            if is_booked(s, e):
                self.q2.append(
                    [max(start, s), min(end, e)] # this is the part where clash happens. Saved in q2 so that we reject double booking. 
                )
        
        self.q1.append([start, end])
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)