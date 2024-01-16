class RandomizedSet:

    def __init__(self):
        self.data, self.pos = [], {}

    def insert(self, val: int) -> bool:
        if val in self.pos: return False
        
        self.data.append(val)
        self.pos[val] = len(self.data)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos: return False
        
        val_pos, last_pos = self.pos[val], self.pos[self.data[-1]]
        self.data[val_pos] = self.data[-1]
        self.pos[self.data[-1]] = val_pos
        self.data.pop()
        self.pos.pop(val, 0)
        return True

    def getRandom(self) -> int:
        return self.data[random.randint(0, len(self.data)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()