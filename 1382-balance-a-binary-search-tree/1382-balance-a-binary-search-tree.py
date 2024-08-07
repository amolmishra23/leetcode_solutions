# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root):
        
        def inorder(node):
            if not node: return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        ns = inorder(root)
        
        def build(l, r):
            if l > r: return None
            m = (l + r) // 2
            root = TreeNode(ns[m])
            root.left, root.right = build(l, m-1), build(m + 1, r)
            return root
        
        return build(0, len(ns) - 1)