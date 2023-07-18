class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.deque = deque()
        self.map = {}

    def get(self, key: int) -> int:
        if key not in self.map: return -1
        self.deque.remove(key)
        self.deque.append(key)
        return self.map[key]

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.deque.remove(key)
        else:
            if len(self.deque) == self.cap:
                del self.map[self.deque.popleft()]
        
        self.map[key] = value
        self.deque.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)