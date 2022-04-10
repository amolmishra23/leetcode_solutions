class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors = [v1, v2]
        self.queue = deque()
        
        for idx, vector in enumerate(self.vectors):
            if len(vector)>0:
                self.queue.append((idx, 0))

    def next(self) -> int:
        if self.queue:
            vec_index, elem_index = self.queue.popleft()
            next_idx = elem_index+1
            if next_idx < len(self.vectors[vec_index]):
                self.queue.append((vec_index, next_idx))
            return self.vectors[vec_index][elem_index]
        
        raise Exception
            
    def hasNext(self) -> bool:
        return len(self.queue) > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())