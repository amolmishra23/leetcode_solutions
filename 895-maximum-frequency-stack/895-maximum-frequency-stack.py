class Element:
    def __init__(self, num, freq, seq):
        self.num = num
        self.freq = freq
        self.seq = seq
        
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq > other.freq
        return self.seq > other.seq

class FreqStack(object):

    def __init__(self):
        self.maxHeap = []
        self.frequencies = {}
        self.sequenceNumber = 0

    def push(self, x):
        # Increment frequency count
        if x not in self.frequencies:
            self.frequencies[x] = 0
        self.frequencies[x] += 1
        
        # Push x on the maxHeap
        heappush(self.maxHeap, Element(x, self.frequencies[x], self.sequenceNumber))
        
        # Increment sequence number
        self.sequenceNumber += 1
        

    def pop(self):
        e = heappop(self.maxHeap)
        self.frequencies[e.num] -= 1
        
        return e.num