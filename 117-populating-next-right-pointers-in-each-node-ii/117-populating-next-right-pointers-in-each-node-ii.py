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
        if root is None: return root
        q = deque([root])
        res = []
        while q:
            len_ = len(q)
            prev = None
            
            for _ in range(len_):
                front = q.popleft()
                if prev: prev.next = front
                
                if front.left: q.append(front.left)
                if front.right: q.append(front.right)
                prev = front
                    
        return root