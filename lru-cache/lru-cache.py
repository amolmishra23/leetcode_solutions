class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        """
        Dictionary is just to maintain constant lookup and return the object
        We maitain a doubly LL which helps us decide which element to delete, when there is overflow.
        Data is copied both the places. But we use both effectively to achieve our goal of LRU cache
        """
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """
        During get operation, we remove the node wherever in the LL
        Add it to end of the list, as that shows its recently used element
        Maintaining the LRU property
        """
        if key in self.dic:
            node = self.dic[key]
            self.__remove(node)
            self.__add(node)
            return node.val
        return -1

    def __remove(self, node):
        """
        It removes the node, wherever present in the linkedlist. 
        As its double LL, easy to do so.
        """
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        
    def __add(self, node):
        """
        0->a->b->c->0
        c.prev = b
        c.next = 0
        
        c.next = d
        0.prev = d
        d.prev = c
        d.next = 0
        
        Basically in the end
        0->a->b->c->d->0
        """
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
        
    def put(self, key: int, value: int) -> None:
        """
        We check if val is present, we remove the old value.
        Add the new value
        If the size is exceeding, we then delete the element from front of the LL. 
        """
        if key in self.dic: self.__remove(self.dic[key])
        new_node = Node(key, value)
        self.__add(new_node)
        self.dic[key] = new_node
        
        if len(self.dic)>self.capacity:
            n = self.head.next
            self.__remove(n)
            del self.dic[n.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)