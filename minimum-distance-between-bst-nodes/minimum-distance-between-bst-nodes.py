# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            if node is None: return
            inorder(node.left)
            self.res = min(self.res, node.val-self.prev)
            self.prev = node.val
            inorder(node.right)
            
        self.res, self.prev = float('inf'), float('-inf')
        inorder(root)
        return self.res