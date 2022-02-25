"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.q = deque()
        self.res = []
        
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None: return []
        self.q.append(root)
        while self.q:
            curr = []
            len_ = len(self.q)

            for _ in range(len_):
                node = self.q.popleft()
                curr.append(node.val)
                
                for x in node.children:
                    self.q.append(x)
                    
            self.res.append(curr)
            
        return self.res