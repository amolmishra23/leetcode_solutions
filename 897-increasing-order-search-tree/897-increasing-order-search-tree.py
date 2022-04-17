# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if root is None: return
            
            inorder(root.left)
            self.prev.right = root
            root.left = None
            self.prev = root
            inorder(root.right)
            
        temp = self.prev = TreeNode(0)
        inorder(root)
        return temp.right