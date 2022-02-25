"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def dfs(self, head):
        # prev to the node we are currently processing,
        prev = None
        
        # iterating till end of the LL
        # ideally if no child nodes exist, we just going to else condition head=head.next
        # and eventually we will return last to tail node.
        
        # but we may have child nodes. so we keep travelling entire child node, and return its last pointer.
        # then make the necessary adjustments, to shift pointers. 
        # first in and around tail, then in and around head. 
        # finally reset the head to point to tail.next, so that processing of nodes can be resumed there. 
        while head is not None:
            prev = head
            if head.child is not None:
                # playing around with the tail node
                tail = self.dfs(head.child)
                tail.next = head.next
                if head.next is not None:
                    head.next.prev = tail
                
                # now playing around with start node
                head.next = head.child
                head.child.prev = head
                head.child = None
                
                # reset pointers to continue iteration
                prev = tail
                head = tail.next
            else:
                head = head.next
        
        return prev
        
        
    def flatten(self, head: 'Node') -> 'Node':
        self.dfs(head)
        return head