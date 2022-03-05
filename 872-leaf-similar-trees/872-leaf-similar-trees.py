# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def preorder(root, res):
            if root.left is None and root.right is None: res.append(root.val); return
            if root.left: preorder(root.left, res)
            if root.right: preorder(root.right, res)
        
        res1, res2 = [], []
        preorder(root1, res1)
        preorder(root2, res2)
        return res1 == res2