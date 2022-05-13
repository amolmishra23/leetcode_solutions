"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        q = deque([root])
        
        while q:
            prev, l = None, len(q)
            for _ in range(l):
                curr = q.popleft()
                if prev: prev.next = curr
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
                prev = curr
            if prev: prev.next = None
            
        return root