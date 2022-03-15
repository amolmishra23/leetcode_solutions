class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.dq = collections.deque()
        self.valueMap = {}

    def get(self, key: int) -> int:
        if key not in self.valueMap:
            return -1
        self.dq.remove(key)
        self.dq.append(key)
        
        return self.valueMap[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.valueMap:
            if len(self.dq) == self.cap:
                del self.valueMap[self.dq.popleft()]
        else:
            self.dq.remove(key)
        
        self.dq.append(key)
        self.valueMap[key] = value