# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find_lca(self, root, p, q):
        if root in {None, p, q}: return root

        left, right = self.find_lca(root.left, p, q), self.find_lca(root.right, p, q)

        if left is not None and right is not None: return root

        return left or right
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':        
        if root is None or p is None or q is None: return None
        
        res = self.find_lca(root, p, q)
        
        if res == p:
            return res if self.find_lca(p, q, q)==q else None
        elif res == q:
            return res if self.find_lca(q, p, p)==p else None
        
        return res