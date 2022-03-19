class Element:
    def __init__(self, num, freq, seq):
        self.num = num
        self.freq = freq
        self.seq = seq
        
    def __lt__(self, other):
        if self.freq!=other.freq:
            return self.freq>other.freq
        return self.seq>other.seq

class FreqStack:

    def __init__(self):
        self.max_heap = []
        self.freq = defaultdict(int)
        self.seq = 0

    def push(self, val: int) -> None:
        self.freq[val]+=1
        if self.freq[val]>0: heappush(self.max_heap, Element(val, self.freq[val], self.seq))
        self.seq += 1

    def pop(self) -> int:
        res = heappop(self.max_heap)
        self.freq[res.num]-=1
        return res.num


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()