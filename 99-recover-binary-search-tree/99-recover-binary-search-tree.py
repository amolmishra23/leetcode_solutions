# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.first, self.second = None, None
        self.prev = TreeNode(float('-inf'))
        
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root):
            if root:
                inorder(root.left)
                if self.prev.val >= root.val:
                    self.first = self.first or self.prev
                    self.second = root
                self.prev = root
                inorder(root.right)
        
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val