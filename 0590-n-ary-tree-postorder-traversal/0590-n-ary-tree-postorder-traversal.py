"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def solve(root):
            if root is None: return
            for node in root.children:
                solve(node)
            self.res.append(root.val)
            
        self.res = []
        solve(root); return self.res