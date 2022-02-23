"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        def print_list(curr):
            while curr:
                print (curr.val)
                curr = curr.next
        
        cache = {}
        curr, new_head = head, Node(0)
        prev = new_head

        while curr:
            new_node = Node(curr.val)
            cache[curr] = new_node
            prev.next = new_node
            prev = new_node
            curr = curr.next
        
        curr, new_curr = head, new_head.next
        while curr:
            new_curr.random = cache.get(curr.random)
            curr = curr.next
            new_curr = new_curr.next
            
        return new_head.next
        