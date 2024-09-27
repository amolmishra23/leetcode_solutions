class MyCalendarTwo:
    def clash(self, e1, e2):
        max_start = max(e1[0], e2[0])
        min_end = min(e1[1], e2[1])
        
        return max_start<min_end
    
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def book(self, start: int, end: int) -> bool:
        ne = (start,end)
        for e in self.q2:
            if self.clash(ne, e): return False
            
        for e in self.q1:
            if self.clash(ne, e):
                self.q2.append(
                    (max(start,e[0]),min(end,e[1]))
                )
            
        self.q1.append(ne)
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)