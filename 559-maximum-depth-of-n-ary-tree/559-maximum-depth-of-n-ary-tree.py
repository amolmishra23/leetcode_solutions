"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def solve(self, node, l):        
        for x in node.children:
            self.res = max(self.res, l+1)
            self.solve(x, l+1)
        
    def maxDepth(self, root: 'Node') -> int:
        if root is None: return 0
        self.res = 1
        self.solve(root, 1)
        return self.res
        