class LockingTree:

    def __init__(self, parent: List[int]):
        self.child_to_parent = parent
        self.locked = [None]*len(parent)
        self.parent_to_child = defaultdict(list)
        
        for i in range(1, len(parent)):
            self.parent_to_child[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num]: return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num]!=user: return False
        self.locked[num] = None
        return True

    def upgrade(self, num: int, user: int) -> bool:
        i = num
        
        while i!=-1:
            if self.locked[i]: return False
            i = self.child_to_parent[i]
            
        locked_count, q = 0, deque([num])
        
        while q:
            n = q.popleft()
            if self.locked[n]:
                self.locked[n] = None
                locked_count += 1
            q.extend(self.parent_to_child[n])
            
        if locked_count:
            self.locked[num] = user
            return True
        
        return False
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)