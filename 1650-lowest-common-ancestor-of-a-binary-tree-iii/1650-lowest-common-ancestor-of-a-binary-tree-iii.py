"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        s = set()
        
        while p!=None: 
            s.add(p)
            p = p.parent
            
        while q!=None and q not in s:
            s.add(q)
            q = q.parent
            
        return q